# degw
Non parametric differentially gene expression analysis
```
Usage:
  DEGwilcox <gene_expression_matrix> <sample_metadata> [--condition=<condition>] [--g1=<g1>] [--g2=<g2>] [--min_exp=<min_exp>] [--min_samples_ratio=<min_sampes_ratio>]

The file <gene_expression_matrix> shoud have gene names on the first column and samples as column names.
The expression data are expected as raw (not normalized) data.

The file <sample_metadata> shoud have gene sample names on the first column.

Options:
  --condition <condition>        Name of dichotomous variable column in the metadata file to discriminate the two group of samples [default: condition].
  --g1 <g1>                      Level 1 of the dichotomous variable, indentifing group1_samples samples [default: case].
  --g2 <g2>                      Level 2 of the dichotomous variable, indentifing group2_samples samples [default: control].
  --min_exp <min_exp>            Minimum expression levels (cpm) to consider a gene as expressed [default: 1].
  --min_samples_ratio <min_sampes_ratio>            If less that <min_exp_sampes_ratio> (rounded up) samples show a gene expressed in at least one group, then the gene if filtered out as not expressed [default: 0.5].
' -> doc
```
