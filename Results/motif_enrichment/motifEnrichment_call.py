
# Import
import os

# Parameters
organism="--organism hg19"
promoter_length="--promoter-length 1000"
maximum_association_length="--maximum-association-length 50000"
multiple_test_alpha="--multiple-test-alpha 0.05"
processes="--processes 1"
print_thresh="--print-thresh 1.0"
bigbed="--bigbed"

###################################################################################################
# RANDOM BACKGROUND
###################################################################################################

# Parameters
inputMatrix="/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/matrix/ME_random_background2.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/random_background/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/random_background/"

# Execution
myL = "ME_RAND"
clusterCommand = "bsub -J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
clusterCommand += "-W 100:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)


###################################################################################################
# PROMOTER BACKGROUND
###################################################################################################

inList = ["LPS_LPS_LPS_n_DOWN", "LPS_LPS_LPS_n_UP"]
for inName in inList:

  # Parameters
  inputMatrix="/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/matrix/ME_"+inName+".txt"
  matchLoc="/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/all_promoter_background/"+inName+"/"
  output_location="--output-location /work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment/extra/all_promoter_background/"+inName+"/"

  # Execution
  myL = "ME_PROM"
  clusterCommand = "bsub -J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt "
  clusterCommand += "-W 100:00 -M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
  clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
  clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
  os.system(clusterCommand)


