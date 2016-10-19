#Week7

###Compare the variants for BRCA1 and BRCA2 trimmed with VQSR to the clinical risks list of BRCA Exchange database.

1.Download the Clinical Risks list of [BRCA Exchange database for BRCA1](http://vannberg.biology.gatech.edu/data/ahcg2016/BRCA/BRCA1_brca_exchange_variants.csv) and [BRCA Exchange database for BRCA2](http://vannberg.biology.gatech.edu/data/ahcg2016/BRCA/BRCA2_brca_exchange_variants.csv).

2.Compare vcf file with data columns obtained from hg37 reference genome (hg19 was used for VCF).

```{sh}
cd ../scripts
python3 compare.py ../database/BRCA1_brca_exchange_variants.csv ../assignment5/output_github/output.recalibrated.filtered.vcf
python3 compare.py ../database/BRCA2_brca_exchange_variants.csv ../assignment5/output_github/output.recalibrated.filtered.vcf
```
To run the python script, download the vcf package. It may be that you will not be able to do that on the virtual box. I did on muy mac. If your version of python is 2.7, use this command

```{sh}
python compare2.7.py BRCA1_brca_exchange_variants.csv output.recalibrated.filtered.vcf
python compare2.7.py BRCA2_brca_exchange_variants.csv output.recalibrated.filtered.vcf
```
