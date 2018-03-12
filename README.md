# SILVA taxonomy parser

A script to parse SILVA taxonomy and format it to keep only basic seven levels of taxonomy (Kingdom, Phylum, Class, Order, Family, Genus, Species).

For any queries, please either ask on github issue page or send an email to Nidhi Shah (nidhi@cs.umd.edu).

###Running the script
```
python parser.py -h
usage: parser.py [-h] -tax TAXONOMY_FILE -map MAP_FILE [-out OUTPUT_FILE]

A script to parse SILVA taxonomy into seven levels of taxonomy

optional arguments:
  -h, --help            show this help message and exit
  -tax TAXONOMY_FILE, --taxonomy_file TAXONOMY_FILE
                        taxonomy information for each database sequence. e.g.
                        taxmap_slv_ssu_ref_128.txt in SILVA release v.128
  -map MAP_FILE, --map_file MAP_FILE
                        A file mapping taxonomy name with taxid and level e.g.
                        tax_slv_ssu_128.txt in SILVA release v.128
  -out OUTPUT_FILE, --output_file OUTPUT_FILE
                        output file name (default - silva_taxonomy.tsv)
```