from subprocess import call

dl_file_template = "ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/ALL.{chromosome}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz"

for chromosome in ["chr{}".format(i) for i in list(range(1, 23)) + ["X", "Y"]]:
    dl_file = dl_file_template.format(chromosome=chromosome)
    command = "wget -P data {}".format(dl_file)
    call(command, shell=True)

call(
    "wget -P data ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502/integrated_call_samples_v3.20130502.ALL.panel",
    shell=True)
