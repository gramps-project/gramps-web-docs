# Using Gramps Web for Y-DNA Analysis

!!! note "Note"
    This feature requires Gramps Web API version 3.3.0 or later and Gramps Web frontend version 25.9.0 or later.

The Y-DNA view in Gramps Web can use raw Y chromosome single nucleotide polymorphism (SNP) data to determine a person's most likely Y-DNA haplogroup and display the derived ancestors in the human Y chromosome tree along with timing estimates.

## How to obtain and store the Y-DNA SNP data

To obtain the Y-DNA SNP data, you need to have a Y-DNA test performed through a genetic testing service. The result is represented as a set of mutations (SNPs), each identified by a string (e.g. `R-BY44535`) and a `+` or `-` sign indicating whether the mutation is present or absent. Gramps Web expects the string of all tested SNPs in the format `SNP1+, SNP2-, SNP3+,...` to be stored in a person attribute of custom type `Y-DNA` (case sensitive). You can either manually create this attribute in Gramps Web or Gramps Desktop, or navigate to the Y-DNA view in Gramps Web and click the blue "Add" button, select the person to add the data to, and paste the SNP string. In any case, the data will be stored as a person attribute in your Gramps database.

[See below](#instructions-for-obtaining-snp-data-from-testing-services) for instructions on how to obtain the SNP data from various testing services.

## How it works

Once a person has a `Y-DNA` attribute containing the SNP data, Gramps Web will use the open-source [yclade](https://github.com/DavidMStraub/yclade) Python library to determine the person's most likely position on the human Y chromosome tree. The tree has been created by the [YFull](https://www.yfull.com/) project based on tens of thousands of Y-DNA tests. Note that Gramps Web uses a local copy of the YFull tree, so no data is sent to any third party.

The tree is traversed from the root to the leaves, and at each node, the SNPs associated with that node are compared to the person's positively and negatively tested SNPs, and the appropriate branch is followed.

The final result is a succession of clades from the root of the tree (the [Y-chromosomal "Adam"](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)) to the most derived clade that is consistent with the person's SNP data. Each clade has an estimated age based on the ages of the samples in the YFull database that belong to that clade.

Since Y chromosomes are inherited from father to son, this succession corresponds to an excerpt of the person's patrilineal ancestry.

## How to interpret the results

The most important piece of information is the person's most likely haplogroup, shown at the top of the page. The name is linked to the corresponding page on the [YFull](https://www.yfull.com/) website, which contains more information, such as the country of origin of tested samples belonging to that haplogroup.

In the patrineal ancestor tree shown in Gramps Web, the box directly above the tested person is the most recent common ancestor (MRCA) of all tested samples belonging to the person's haplogroup. The date shown for this ancestor is his estimated approximate birth date. The ancestor above him is the ancestor where the mutation defining this haplogroup first appeared.

Due to the slow mutation rate of Y chromosomes, the MRCA can be many hundreds of years in the past. For rare haplogroups (i.e. halogroups where few people have been tested so far), it can even be thousands of years.


## Instructions for obtaining SNP data from testing services

### [YSEQ](https://www.yseq.net/)

Once logged in to "My Account", go to "My Results / View my Alleles" and navigate to the bottom of the page. The text field " Allele list compact" has been added specifically for Gramps Web and is in exactly the right format for pasting into the `Y-DNA` attribute.