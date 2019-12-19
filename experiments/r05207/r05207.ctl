## Control file for teh 191211 kinase experiment

# experiment folder - where are the files?
experiment_folder:/Users/jacob.cooper/kinase_assay_builder/experiments/r05207/

# compound list (.txt) (relative to experiment folder path)
compound_list:r05207_compound_list.txt

# source plate list (.csv) list of all the source plates and their barcodes. Each entry needs a corresponding .csv that says what is on that source plate
source_plates:r05207_name_bc.csv

# destination plate list (.csv) list of all the source plates and their barcodes. can be "none"
destination_plates:r05207_dest.csv

# compounds per well
compounds_per_well:5

# replicate per compound
replicate_per_compound:5

# experiment replicates
experiment_repliates:1

# transfer volume
transfer_volume:2.5
