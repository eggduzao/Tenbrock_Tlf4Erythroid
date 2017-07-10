
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
inputMatrix="/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/matrix/ME_random_background.txt"
matchLoc="/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/results/random_background/"
output_location="--output-location /work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/results/random_background/"

# Execution
myL = "ME_RAND"
clusterCommand = "bsub -J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt -W 100:00 "
clusterCommand += "-M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
os.system(clusterCommand)


###################################################################################################
# PROMOTER BACKGROUND
###################################################################################################

inList = ["M2c_macrophage_down", "M2c_macrophage_up"]
for inName in inList:

  # Parameters
  inputMatrix="/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/matrix/ME_"+inName+".txt"
  matchLoc="/work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/results/all_promoter_background/"+inName+"/"
  output_location="--output-location /work/eg474423/eg474423_Projects/trunk/Tlf4Erythroid/Results/motif_enrichment_m2c_macrophage/results/all_promoter_background/"+inName+"/"

  # Execution
  myL = "ME_PROM"
  clusterCommand = "bsub -J "+myL+" -o "+myL+"_out.txt -e "+myL+"_err.txt -W 100:00 "
  clusterCommand += "-M 24000 -S 100 -P izkf -R \"select[hpcwork]\" ./motifAnalysis_pipeline.zsh --enrichment "
  clusterCommand += organism+" "+promoter_length+" "+maximum_association_length+" "+multiple_test_alpha+" "
  clusterCommand += processes+" "+output_location+" "+print_thresh+" "+bigbed+" "+inputMatrix+" "+matchLoc
  os.system(clusterCommand)


