#! /usr/bin/env python3

import datetime
import pandas as pd

def find_compound_info(compound, s_plates, dest_plate):
    
    info = {
        'Source' : None,
        'Source Plate Barcode' : None,
        'Source Well' : None,
        'Destination' : None,
        'Destination Plate Barcode' : None,
        'Destination Well' : None,
        'Transfer Volume' : None,
        'Concentration' : None,
        'Reagent ID' : None,
        'Printing ID' : None,
        'Layer' : None,
        'Updated At' : str(datetime.datetime.now()),
        'Printed At' : None,
        'REC ID' : None,        
    }

    for s in s_plates:
        ent = s_plates[s].loc[s_plates[s]['rec_id'] == compound]
        if len(ent['rec_id'].values) != 0:
            info['Source'] = s.split(';')[0]
            info['Source Plate Barcode'] = s.split(';')[1]
            info['Source Well'] = ent['address'].values[0]
            info['Concentration'] = ent['concentration'].values[0]
            info['Reagent ID'] = ent['reagent_id'].values[0]
            info['Layer'] = 'treatment'
            info['REC ID'] = ent['rec_id'].values[0]


    return info
