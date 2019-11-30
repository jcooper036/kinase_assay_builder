#! /usr/bin/env python3

import copy

class Plate(object):
    """
    Represents a 1536 well plate

    """

    def __init__(self):

        self.rows = {}
        self.cols = {}
        self.wells = {}
        self.name = None
        self.barcode = None

        for r in base_rows:
            self.rows[r] = {
                    'layer' : None,
                    'wells' : []
                    }
        for c in base_cols:
            self.cols[c] = {
                    'layer' : None,
                    'wells' : []
                    }
        
        for r in self.rows:
            for c in self.cols:
                # this should contain null for every possible output
                self.rows[r]['wells'].append(r+c)
                self.cols[c]['wells'].append(r+c)

                # self.wells[well][compound] = compound_info
                self.wells[r+c] = {}
    
    def add_compound(self, well, compound, compound_info):
        self.wells[well][compound] = copy.deepcopy(compound_info)
        self.wells[well][compound]['Destination'] = self.name
        self.wells[well][compound]['Destination Plate Barcode'] = self.barcode
        self.wells[well][compound]['Destination Well'] = well
        self.wells[well][compound]['Transfer Volume'] = 40


base_rows = ['B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE']

base_cols = ['02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47']


### full, without the edges removed
# base_rows = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AD','AE','AF']

# base_cols = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48']
