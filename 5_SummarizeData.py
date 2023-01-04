#!/usr/bin/env python

import sys
import argparse

parser = argparse.ArgumentParser()
# required
parser.add_argument('-o', '--OutFileName', required = True, help = "Prefix name of output csv files")
parser.add_argument('-b', '--BaseFileNames', required = True, help = "File containing base file names of all sample files")
parser.add_argument('-r', '--Rank', required = True, help = "Rank to be analyzed (INT from 0 to 6 [kingdom to species])")
args = parser.parse_args()

# get list of all taxa at rank of interest
TaxLst = []
with open(args.BaseFileNames, 'r') as Inputs:
	for iLine in Inputs:
		with open(iLine.strip(), 'r') as File:
			for fLine in File:
				tax = fLine.split('\t')[1].strip()
				if len(tax.split(';')) >= (int(args.Rank)+1):
					if tax.split(';')[int(args.Rank)] not in TaxLst:
						if tax.split(';')[int(args.Rank)] != '':
							TaxLst.append(tax.split(';')[int(args.Rank)])

TmpTaxDct = {} # holds additive count per tax per file
TaxDct = {} # holds final count per tax per file in list form

# populate TmpTaxDct 
TaxDct['aaa_header'] = []
for i in TaxLst:
	TaxDct[i] = []

# run through each file, add hits to TmpTaxDct, add final counts to TaxDct
with open(args.BaseFileNames, 'r') as Inputs:
        for iLine in Inputs:
		TaxDct['aaa_header'].append(iLine.strip().split('.')[0])
		for i in TaxLst:
		        TmpTaxDct[i] = 0
                with open(iLine.strip(), 'r') as File:
                        for fLine in File:
                                tax = fLine.split('\t')[1].strip()
                                if len(tax.split(';')) >= (int(args.Rank)+1):
					if tax.split(';')[int(args.Rank)] != '':
						TmpTaxDct[tax.split(';')[int(args.Rank)]] += 1
		for key, value in TmpTaxDct.items():
			TaxDct[key].append(str(value))

with open(args.OutFileName, 'w') as OutFile:
	for key, value in sorted(TaxDct.items()):
		OutFile.write(str(key) + ',' +  ','.join(value) + '\n')
