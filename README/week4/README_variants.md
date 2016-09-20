##Week4

#Find variants in common between the ones we found with the pipeline and the one from Genome in a Bottle project. 

1.Go to the repository folder

2.Download an Illumina kit to capture exomes from Illumuina website. Go to http://support.illumina.com/sequencing/sequencing_kits/nextera-rapid-capture-exome-kit/downloads.html and choose one kit beetween Nextera Rapid Capture Exome v1.2 and Nextera Rapid Capture Exome 

```{sh}
cd files
wget http://support.illumina.com/content/dam/illumina-support/documents/documentation/chemistry_documentation/samplepreps_nextera/nexterarapidcapture/nexterarapidcapture_exome_targetedregions.bed
```

3.Download the variants found with our pipeline

```{sh}
wget http://vannberg.biology.gatech.edu/data/variants.vcf
```

4.Grab only the variants that are in exome regions of the .vcf file

```{sh}
bedtools intersect -wb -a nexterarapidcapture_exome_targetedregions.bed -b variants.vcf > exome_variants.vcf
```

5.Download all the variants found in the Genome in a Bottle project: go to https://github.com/genome-in-a-bottle/giab_latest_release, click on 'latest release for NA12878_HG001' and enter as a guest. Then, download and gunzip the variants file.

```{sh}
wget NA12878_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-Solid-10X_CHROM1-X_v3.3_highconf.vcf.gz
gunzip NA12878_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-Solid-10X_CHROM1-X_v3.3_highconf.vcf.gz
```
6.Write a python script to remove 'chr' from variants.vcf and save in exome_variants1.vcf

7.Safe the common and not common variants in a file. When you see a '.' this means that the variant is not in common.

```{sh}
bedtools -wao intersect -a NA12878_GIAB_highconf_CG-IllFB-IllGATKHC-Ion-Solid-10X_CHROM1-X_v3.3_highconf.vcf -b exome_variants1.vcf > not_and_common_variants
```

