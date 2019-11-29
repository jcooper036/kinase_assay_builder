# Kinase Assay Design
For this project, we need to design a scheme for distriubting multple compounds across wells. In this exerpiment, we want to have a mix of compounds per well. Each compound needs to be replicated five times, but each replicat needs to be paired with a different compound. At the end of the experiment there will always be some leftover compounds, but they can just go in their own wells.

Control file settings:
    - experiment_folder
        - tells the program where to look for all these different files
    - Compound list
        - text file that is a list of compounds
        - need to make sure that they are present in a source plate
    - source plates
        - csv of the source plate names / barcodes
        - each source plate also needs a csv that has all the compounds in it by position
    - destination plates (optional)
        - csv of the source plate names / barcodes
        - usually run it once without this to tell you how many destination plates you need
    - compounds per well
    - replicate per compound
    - experiment repliate
        - allows you to replicate the whole thing over again
    
Outputs
    - ECHO picklist (.csv)
    - metadata csv