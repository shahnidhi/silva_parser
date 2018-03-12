"""
-----------------------------------------------------------------------------------------
This script creates a tsv file with seven levels of taxonomy for SILVA database sequences.

Written by N. R. Shah [nidhi@cs.umd.edu] in Mar 2018.
-----------------------------------------------------------------------------------------
"""

import sys
import argparse

def main():
	parser = argparse.ArgumentParser(description="A script to parse SILVA taxonomy into seven levels of taxonomy")
	parser.add_argument("-tax","--taxonomy_file",help="taxonomy information for each database sequence. e.g. taxmap_slv_ssu_ref_128.txt in SILVA release v.128",required=True)
	parser.add_argument("-map","--map_file", help="A file mapping taxonomy name with taxid and level e.g. tax_slv_ssu_128.txt in SILVA release v.128",required=True)
	parser.add_argument("-out","--output_file", help="output file name (default - silva_taxonomy.tsv)",default="silva_taxonomy.tsv",required=False)
	args = parser.parse_args()

	reqd_levels = {}
	reqd_levels['domain'] = 0; reqd_levels['phylum'] = 1; reqd_levels['class'] =  2; reqd_levels['order'] = 3; reqd_levels['family'] = 4; reqd_levels['genus'] = 5;
	mappingname = {}
	doublemap = {}
	for i in xrange(0,6):
		doublemap[i] = {}
	mappingid = {}
	with open(args.map_file,'r') as f:
		for line in f:
			val = line.strip().split(';')
			name = val[-2]
			val2 = val[-1].split('\t')
			if val2[2] in reqd_levels.keys():
				mappingname[name] = reqd_levels[val2[2]]
				mappingid[name] = int(val2[1])
				# doublemap[reqd_levels[val2[2]]][name] = reqd_levels[val2[2]]
	fw = open(args.output_file,'w') 
	fq = open(str(args.output_file).split('.')[0]+'_taxid.tsv','w')
	with open(args.taxonomy_file,'r') as f:
		for line in f:
			val = line.strip().split('\t')
			if val[0] == 'primaryAccession':
				continue
			taxa = val[3].split(';')
			new_taxa = {}
			for i in taxa:
				if i in mappingname.keys():
					new_taxa[mappingname[i]] = i 
			linetoprint = str(val[0])+'\t'
			linetoprintid = str(val[0])+'\t'
			for j in xrange(0,6):
				if j in new_taxa.keys():
					linetoprint = linetoprint + str(new_taxa[j]) + ';'
					linetoprintid = linetoprintid + str(mappingid[new_taxa[j]])+';'
				else:
					linetoprint = linetoprint + "NA;"
					linetoprintid = linetoprintid +"0;"
			linetoprint += str(val[4])
			linetoprintid += str(val[5])
			fw.write(linetoprint+'\n')
			fq.write(linetoprintid+'\n')


	fw.close()
	fq.close()
			




if __name__ == "__main__":
	main()