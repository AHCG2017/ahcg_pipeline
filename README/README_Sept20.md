##Week 5


#Find exomes regions from Otogenetics dataset

###Otogenetics dataset
![Alt text](http://www.otogenetics.com/forms/Breast_Cancer_gene_list.pdf "Otogenetics")

###Steps
1.Create a bed file with exome regions of all the genes. Grab the data from hg19_refGene.txt

```{sh}
grep 'NM_000044\|NM_000051\|NM_000465\|NM_007298\|NM_000059\|NM_032043\|NM_001080124\|NM_004360\|NM_001005735\|NM_002485\|NM_024675\|NM_000314\|NM_005732\|NM_001164269\|NM_000455\|NM_000660\|NM_000546' hg19_refGene.txt > otogenetics.txt
```
2.Use the pyton script (split_colomns.py) to convert the TXT file in the BED format

BED Format
chr '\t'  seq start '\t'  seq end 
(https://genome.ucsc.edu/FAQ/FAQformat.html - format1)

3.Run the script and save the output

```{sh} 
python split_colomns.py > otogenetics.bed
```

4.Generate the VCF file from the BED file

```{sh}
bedtools intersect -wb -a otogenetics.bed -b variants.vcf > otogenetics.vcf
```
