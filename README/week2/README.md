
##Week 2
#Find the exons of NM_007294 (BRCA1) 

##BED input

1.Download the input as TXT file 

```{sh}
wget http://vannberg.biology.gatech.edu/data/ahcg2016/reference_genome/hg19_refGene.txt
```

2.Grab and save only the data from NM_007294

```{sh}
grep NM_007294 hg19_refGene.txt > NM_007294.txt
```

3.Write a script in pyton (split_colomns.py) to convert the TXT file in the BED format
#####BED Format
chr '\t'  seq start '\t'  seq end 

(https://genome.ucsc.edu/FAQ/FAQformat.html - format1)

4.Run the script and save the output

```{sh} 
python split_colomns.py > NM_007294.bed
```
##FASTA INPUT

hg19.fa 

## Extract sequences 
Extract the sequences for each interval defined in the BED input from the FASTA input

```{sh}
bedtools getfasta -fi <FASTA input> -bed <BED input> -fo <OUTPUT>
```

#####For more details (http://bedtools.readthedocs.io/en/latest/content/tools/getfasta.html)
