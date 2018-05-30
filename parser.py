import os 
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
	taxainfo = {}
	presence = {}
	for i in xrange(0,6):
		taxainfo[i] = {}
	
	with open(args.map_file,'r') as f:
		for line in f:
			val = line.strip().split(';')
			name = val[-2]
			val2 = val[-1].split('\t')
			taxid = val2[1]
			taxlevel = val2[2]
			if taxlevel in reqd_levels.keys():
				presence[name] = taxid
				taxainfo[reqd_levels[taxlevel]][name] = taxid

	fw = open(args.output_file,'w') 
	fq = open(str(args.output_file).split('.')[0]+'_taxid.tsv','w')
	with open(args.taxonomy_file,'r') as f:
		for line in f:
			val = line.strip().split('\t')
			if val[0] == 'primaryAccession':
				continue
			taxa = val[3].split(';')
			leveltolook = 0
			new_taxa = {}
			new_taxaid = {}
			for t in taxa:
				if t not in presence.keys():
					continue
				else:
					while leveltolook < 6:
						if t in taxainfo[leveltolook].keys():
							new_taxa[leveltolook] = t
							new_taxaid[leveltolook] = presence[t]
							leveltolook += 1
							break
						else:
							leveltolook += 1

			linetoprint = str(val[0])+'\t'
			linetoprintid = str(val[0])+'\t'
			for j in xrange(0,6):
				if j in new_taxa.keys():
					linetoprint = linetoprint + str(new_taxa[j]) + ';'
					linetoprintid = linetoprintid + str(new_taxaid[j])+';'
				else:
					linetoprint = linetoprint + "NA;"
					linetoprintid = linetoprintid +"0;"
			linetoprint += str(val[4])
			linetoprintid += str(val[5])
			fw.write(linetoprint+'\n')
			fq.write(linetoprintid+'\n')
			# print linetoprint, linetoprintid
			

if __name__ == '__main__':
	main()