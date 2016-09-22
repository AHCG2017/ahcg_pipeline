##Week 5

#Find exomes regions from Otogenetics database

###Otogenetics database

![myimage-alt-tag](https://github.com/Korchmaros/ahcg_pipeline/blob/master/resources/otogenetics.png  "Otogenetics")

####Create a BED file with the exome regions from all the genes in the database.
1.Grab the data from the reference genome (hg19_refGene.txt) and save it on a TXT file.

```{sh}
cd ahcg_pipeline/files/ 
grep 'NM_000044\|NM_000051\|NM_000465\|NM_007298\|NM_000059\|NM_032043\|NM_001080124\|NM_004360\|NM_001005735\|NM_002485\|NM_024675\|NM_000314\|NM_005732\|NM_001164269\|NM_000455\|NM_000660\|NM_000546' hg19_refGene.txt > otogenetics.txt
```
2.Use a pyton script (split_colomns.py) to convert the TXT file in the BED format

BED Format
chr '\t'  seq start '\t'  seq end 
(https://genome.ucsc.edu/FAQ/FAQformat.html - format1)


 ```{sh} 
python split_colomns.py ../files/otogenetics.txt > ../files/otogenetics.bed
```
 
4.Generate the VCF file from the BED file
 
```{sh}
bedtools intersect -wb -a otogenetics.bed -b variants.vcf > otogenetics.vcf
```
