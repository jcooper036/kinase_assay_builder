#! /usr/bin/env python3

class Ctl(object):
    """
    """
    
    def __init__(self, file):
        self.file = file
        self.raw_text = ''
        self.folder = None
        self.compounds = []
        self.sp = []
        self.dp = [] # this is a list of the names
        self.dest_plates = {} # this is where we are going to put plate object
        self.comp_per_well = 5
        self.rep_per_comp = 5
        self.exp_reps = 3

        self.parse_file()

    def parse_file(self):
        
        with open(self.file, 'r') as f:
            for line in f:
                self.raw_text += line
                line = line.rstrip()
                
                if 'experiment_folder:' in line:
                    self.folder = str(line.split(':')[1])
                    if self.folder[-1] != '/':
                        self.folder += '/'
                
                if 'compound_list:' in line:
                    fi = self.folder + str(line.split(':')[1])
                    with open(fi, 'r') as a:
                        for l in a:
                            l = l.rstrip()
                            self.compounds.append(l)
                
                if 'source_plates' in line:
                    fi = self.folder + str(line.split(':')[1])
                    ent = []
                    with open(fi, 'r') as a:
                        for l in a:
                            l = l.rstrip()
                            ent.append(l)
                    self.sp = ent[1:]
                    self.sp = [x.split(',') for x in self.sp]

                
                if 'destination_plates' in line:
                    if str(line.split(':')[1]) != 'none':
                        fi = self.folder + str(line.split(':')[1])
                        ent = []
                        with open(fi, 'r') as a:
                            for l in a:
                                l = l.rstrip()
                                ent.append(l)
                        self.dp = ent[1:]
                        self.dp = [x.split(',') for x in self.dp]


                if 'compounds_per_well' in line:
                    self.comp_per_well = int(line.split(':')[1])
                
                if 'replicate_per_compound' in line:
                    self.rep_per_comp = int(line.split(':')[1])
                
                if 'experiment_repliates' in line:
                    self.exp_reps = int(line.split(':')[1])
                
                if 'transfer_volume:' in line:
                    self.transfer_vol = float(line.split(':')[1])