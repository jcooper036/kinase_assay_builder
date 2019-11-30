#! /usr/bin/env python3

import sys
import os
import random
import pandas as pd
import AssayBuilder as asb

if __name__ == "__main__":
    
    ### load data
    
    # load the control file
    ctl = asb.Ctl(sys.argv[1])

    # load the source plate info. source plate files can be by name or by barcode
    spfiles = {}
    s_plates = {}
    for n in ctl.sp:
        if os.path.isfile(ctl.folder + '/source_plates/' + n[0] + '.csv'):
            spfiles[n[0] + ';' + n[1]] = ctl.folder + '/source_plates/' + n[0] + '.csv'
        if os.path.isfile(ctl.folder + '/source_plates/' + n[1] + '.csv'):
            spfiles[n[0] + ';' + n[1]] = ctl.folder + '/source_plates/' + n[1] + '.csv'
    for splate in spfiles:
        s_plates[splate] = pd.read_csv(spfiles[splate])

    ### check the compound list against the things in the source plates
    sp_compounds = []
    for sp in s_plates:
        sp_compounds += list(s_plates[sp]['reagent_id'].values)
    sp_compounds = set(sp_compounds)
    missing_compounds = [x for x in ctl.compounds if x not in sp_compounds]
    if missing_compounds:
        print(f'WARNING: some compounds are not present in the source plates:{missing_compounds}')
    
    ### build a list that has all the compounds in the random combinations
    compound_combinations = asb.build_combinations(ctl.compounds, ctl.comp_per_well, ctl.rep_per_comp)
    print(f'{len(ctl.compounds)} compounds with {ctl.comp_per_well} compounds per well at {ctl.rep_per_comp} replicates per compound requires {len(compound_combinations)} wells')
    plates_per_exp = int(len(compound_combinations)/1380) + 1
    print(f'{plates_per_exp} plate(s) are needed per replicate of the experiment')

    ### knowing the total number of plates, randomize the order of the wells in those plates
    for i in range(plates_per_exp):
        if not ctl.dp:
            ctl.dest_plates[str(i)+';'+str(i)] = asb.Plate()
            ctl.dest_plates[str(i)+';'+str(i)].name = str(i)
            ctl.dest_plates[str(i)+';'+str(i)].barcode = str(i)
        else:
            ctl.dest_plates[ctl.dp[i][0]+';'+ctl.dp[i][1]] = asb.Plate()
            ctl.dest_plates[ctl.dp[i][0]+';'+ctl.dp[i][1]].name = ctl.dp[i][0]
            ctl.dest_plates[ctl.dp[i][0]+';'+ctl.dp[i][1]].barcode = ctl.dp[i][1]

    well_order = []
    for plate in ctl.dest_plates:
        for well in ctl.dest_plates[plate].wells:
            well_order.append((plate,well))
    random.shuffle(well_order)

    ### then pull the first compound well and the first plate well off the list and assign those compounds to that well
    for idx in range(len(compound_combinations)):
        plate = well_order[idx][0]
        well = well_order[idx][1]
        for comp in compound_combinations[idx]:
            comp_info = asb.find_compound_info(comp, s_plates, plate)
            ctl.dest_plates[plate].add_compound(well, comp, comp_info)

    ### make a picklist from all the different wells in the destination plates that have values
    header = ['Source', 'Source Plate Barcode', 'Source Well', 'Destination', 'Destination Plate Barcode', 'Destination Well', 'Transfer Volume', 'Concentration', 'Reagent ID', 'Printing ID', 'Layer', 'Updated At', 'Printed At', 'REC ID']
    vals = []
    for plate in ctl.dest_plates:
        for well in ctl.dest_plates[plate].wells:
            if ctl.dest_plates[plate].wells[well]:
                for compound in ctl.dest_plates[plate].wells[well]:
                    ent = []
                    for h in header:
                        ent.append(str(ctl.dest_plates[plate].wells[well][compound][h]))
                    vals.append(ent)
    
    ### write the csv
    file = ctl.folder + 'picklist.csv'
    with open(file, 'w') as f:
        f.write(','.join(header))
        f.write('\n')
        for ent in vals:
            f.write(','.join(ent))
            f.write('\n')

                
