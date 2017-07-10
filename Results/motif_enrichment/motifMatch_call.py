
# Import
import os

# Parameters
organism="--organism hg19"
fpr="--fpr 0.0001"
precision="--precision 10000"
pseudocounts="--pseudocounts 0.1"
bigbed="--bigbed"

###################################################################################################
# RANDOM BACKGROUND
###################################################################################################

# Parameters
rand_proportion="--rand-proportion 10"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/random_background/"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/matrix/MM_random_background2.txt"

# Execution
myL = "MM_RAND"
clusterCommand = "bsub -J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 100:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)


###################################################################################################
# PROMOTER BACKGROUND
###################################################################################################

# Parameters
rand_proportion="--rand-proportion 0.0001"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/all_promoter_background/"
inputMatrix="/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/matrix/MM_all_promoter_background2.txt"

# Execution
myL = "MM_PROM"
clusterCommand = "bsub -J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 100:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --matching "
clusterCommand += organism+" "+fpr+" "+precision+" "+pseudocounts+" "+rand_proportion+" "
clusterCommand += output_location+" "+bigbed+" "+inputMatrix
os.system(clusterCommand)


