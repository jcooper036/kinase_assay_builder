#! /user/bin/env python3

import random

def build_combinations(compounds, comp_per_well, rep_per_comp):
    """
    Inputs:
        compounds []
    Returns:
        wells [[]] 
    """

    ## build a list of the compounds by number
    
    wells = [
    [0,1,2,3,4]
    ]

    numbers_done = []

    numbers_left = [(0,1),(1,1), (2,1), (3,1), (4,1)]

    next_number = 5

    seen_with = {
        0 : [1,2,3,4],
        1 : [0,2,3,4],
        2 : [0,1,3,4],
        3 : [0,1,2,4],
        4 : [0,1,2,3],
    }

    while numbers_left:
    
        #new numbers done
        finished = []
        
        # make a a new well
        new_well = []
        
        # try to add the smallest number in that list to the well
        for idx, num in enumerate(numbers_left):
            if num[0] not in new_well:
                if not any([x in seen_with[num[0]] for x in new_well]):
                    if numbers_left[idx][1] < rep_per_comp:
                        new_well.append(num[0])
                        numbers_left[idx] = (num[0], num[1]+1)
        
        # if the length of the well is not 5
        while (len(new_well) < comp_per_well) and (next_number < len(compounds)):
            new_well.append(next_number)
            numbers_left.append((next_number, 1))
            next_number += 1
            
        # add to the "seen_with" dictionary   
        for num in new_well:
            if num in seen_with:
                for onum in new_well:
                    if onum != num:
                        seen_with[num].append(onum)
            else:
                seen_with[num] = []
                for onum in new_well:
                    if onum != num:
                        seen_with[num].append(onum)

        # add the new well
        if new_well:
            wells.append(new_well)
        
        # remove the numbers that are done
        for idx, num in enumerate(numbers_left):
            if numbers_left[idx][1] == rep_per_comp:
                numbers_left.remove(num)

    # convert the ids to compounds
    random.shuffle(compounds)
    comp_wells = []
    for ent in wells:
        new_ent = []
        for val in ent:
            new_ent.append(compounds[val])
        comp_wells.append(new_ent)
   
    return comp_wells