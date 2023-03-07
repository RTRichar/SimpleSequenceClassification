```
ls *L001_R1_001.fastq.gz | while read i
do
  # pull sample identifier from filename
  	a=`echo $i | cut -d'_' -f1-3`
  # merge forward and reverse
  	vsearch --fastq_mergepairs ${a}_R1_001.fastq.gz --reverse ${a}_R2_001.fastq.gz \
		--fastaout ${a}_merged.fa --fastq_allowmergestagger --threads 28
  # calculate alignments
	vsearch --usearch_global ${a}_MrgClp.fa --db ITS2_PlantReferenceDB.fa \
		--id 0.95 --strand both --maxaccepts 100 --maxrejects 50 --maxhits 1 \
		--gapopen 0TE --gapext 0TE --userout ${a}.vsrch70pi.txt \
		--userfields query+target+id+alnlen+mism+opens+qlo+qhi+tlo+thi+evalue+bits+qcov \
		--query_cov 0.8 --threads 28
  # annotate vsearch tabular output with taxonomic lineages
	python 3_VsearchToMetaxa2.py -v ${a}.vsrch70pi.txt \
		-t ITS2_PlantReferenceDB.tax -o ${a}.mtxa2.tax
  # trim annotations based on percent ID match
	python 4_TrimMtxa2IDs.py ${a}.mtxa2.tax ${a}.Trmd.txt
done

ls *.Trmd.txt > BaseNames.txt
python 5_SummarizeData.py -r 5 -b BaseNames.txt -o ITS2_GenusCountTable.csv
```
