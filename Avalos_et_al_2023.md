Code associated with 'Prospects of pollinator community surveillance using terrestrial environmental DNA metagenetics'

#### 28S
```
ls *L001_R1_001.fastq.gz | while read i
do
        a=`echo $i | cut -d'_' -f1-3`
        # merge forward and reverse
        vsearch --fastq_filter ${i} -fastaout ${a}.fa --fastq_truncqual 20 --fastq_minlen 200 --fastq_stripleft 23
        # calculate alignments
        vsearch --usearch_global ${a}.fa --db /fs/project/PAS1063/Avalos_eDNA/eDNA_Database/28S/28S_Amplicons.fasta --id 0.70 \
                --maxaccepts 100 --maxrejects 50 --maxhits 1 --gapopen 0TE \
                --gapext 0TE --userout ${a}.vsrch70pi.txt --userfields query+target+id+alnlen+mism+opens+qlo+qhi+tlo+thi+evalue+bits+qcov \
                --query_cov 0.8 --threads 28
        # annotate vsearch tabular output with taxonomic lineages
        python ./../3_VsearchToMetaxa2.py -v ${a}.vsrch70pi.txt -t /fs/project/PAS1063/Avalos_eDNA/eDNA_Database/28S/28S_Amplicons.tax -o ${a}.mtxa2.tax
        # trim annotations based on percent ID match
        python ./../4_TrimMtxa2IDs.py ${a}.mtxa2.tax ${a}.Trmd.txt
done

ls *.Trmd.txt > BaseNames.txt
python ./../5_SummarizeData.py -b BaseNames.txt -r 5 -o 28S_GenusSummary.csv
```
### COI
```
ls *L001_R1_001.fastq.gz | while read i
do
        a=`echo $i | cut -d'_' -f1-3`
        # merge forward and reverse
        vsearch --fastq_mergepairs ${a}_R1_001.fastq.gz --reverse ${a}_R2_001.fastq.gz --fastaout ${a}_Mrg.fa --fastq_allowmergestagger --threads 28
        vsearch --fastx_filter ${a}_Mrg.fa --fastq_stripleft 20 --fastq_stripright 20 --fastaout ${a}_MrgClp.fa --fastq_minlen 200
        # calculate alignments
        vsearch --usearch_global ${a}_MrgClp.fa --db /fs/project/PAS1063/Avalos_eDNA/eDNA_Database/CO1/Updated_CO1_Amplicons.fasta --id 0.70 \
                --maxaccepts 100 --maxrejects 50 --maxhits 1 --gapopen 0TE \
                --gapext 0TE --userout ${a}.vsrch70pi.txt --userfields query+target+id+alnlen+mism+opens+qlo+qhi+tlo+thi+evalue+bits+qcov \
                --query_cov 0.8 --threads 28
        # annotate vsearch tabular output with taxonomic lineages
        python ./../3_VsearchToMetaxa2.py -v ${a}.vsrch70pi.txt -t /fs/project/PAS1063/Avalos_eDNA/eDNA_Database/CO1/Updated_CO1_Amplicons.tax -o ${a}.mtxa2.tax
        # trim annotations based on percent ID match
        python ./../4_TrimMtxa2IDs.py ${a}.mtxa2.tax ${a}.Trmd.txt
done

ls *.Trmd.txt > BaseNames.txt
python ./../5_SummarizeData.py -b BaseNames.txt -r 5 -o COI_GenusSummary.csv
```
### 16S
```
ls *L001_R1_001.fastq.gz | while read i
do
        a=`echo $i | cut -d'_' -f1-3`
        # merge forward and reverse
        vsearch --fastq_mergepairs ${a}_R1_001.fastq.gz --reverse ${a}_R2_001.fastq.gz --fastaout ${a}_Mrg.fa --fastq_allowmergestagger --threads 28
        vsearch --fastx_filter ${a}_Mrg.fa --fastq_stripleft 18 --fastq_stripright 18 --fastaout ${a}_MrgClp.fa --fastq_minlen 200
        # calculate alignments
        vsearch --usearch_global ${a}_MrgClp.fa --db /fs/project/PAS1063/Avalos_eDNA/eDNA_Database/16S/Updated_16S_Amplicons.fasta --id 0.70 \
                --maxaccepts 100 --maxrejects 50 --maxhits 1 --gapopen 0TE \
                --gapext 0TE --userout ${a}.vsrch70pi.txt --userfields query+target+id+alnlen+mism+opens+qlo+qhi+tlo+thi+evalue+bits+qcov \
                --query_cov 0.8 --threads 28 --strand both
        # annotate vsearch tabular output with taxonomic lineages
        python ./../3_VsearchToMetaxa2.py -v ${a}.vsrch70pi.txt -t /fs/project/PAS1063/Avalos_eDNA/eDNA_Database/16S/Updated_16S_Amplicons.tax -o ${a}.mtxa2.tax
        # trim annotations based on percent ID match
        python ./../4_TrimMtxa2IDs.py ${a}.mtxa2.tax ${a}.Trmd.txt
done

ls *.Trmd.txt > BaseNames.txt
python ./../5_SummarizeData.py -b BaseNames.txt -r 5 -o 16S_GenusSummary.csv
```
