## Control file for sample experiment

# experiment folder - where are the files?
experiment_folder:/Users/jacob.cooper/kinase_assay_builder/experiments/sample/

# compound list (.txt) (relative to experiment folder path)
compound_list:sample_compound_list_1.txt

# source plate list (.csv) list of all the source plates and their barcodes. Each entry needs a corresponding .csv that says what is on that source plate
source_plates:source_names_and_barcodes.csv

# destination plate list (.csv) list of all the source plates and their barcodes. can be "none"
destination_plates:none

# compounds per well
compounds_per_well:5

# replicate per compound
replicate_per_compound:5

# experiment replicates
experiment_repliates:3
