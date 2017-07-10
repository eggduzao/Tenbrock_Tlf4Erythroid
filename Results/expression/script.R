library(GEOquery)

mygeomat <- getGEO("GSE61477", GSEMatrix=TRUE)

pheno=pData(phenoData(mygeomat[[1]]))

pheno$description[1]=pheno$description[2]

data=exprs(mygeomat[[1]])
annot=fData(mygeomat[[1]])

library(limma)

design <- model.matrix(factor(c(1,1,1,2,2,2,3,3,3,4,4,4)))
colnames(design) <- c("A", "B", "C","D")
fit <- lmFit(data, design)
contrast.matrix <- makeContrasts(B-A,C-A,D-A, levels=design)
fit2 <- contrasts.fit(fit, contrast.matrix)
fit2 <- eBayes(fit2)


results_05 <- decideTests(fit2,lfc=1)

results=topTable(fit2, coef=1, number=dim(data)[1], adjust="BH",sort.by="none")

data_final=as.data.frame(data)
data_final$fold=results$logFC
data_final$Symbol=annot[,10]
data_final$de=results_05[,1]

data_final$h1=rowMeans(data_final[,c(1:4)])
data_final$k562=rowMeans(data_final[,c(5:25)])
data_final$symbol_clean=as.character(lapply(strsplit(as.character(data_final$Symbol), split="//"), "[", 2))

write.table(data_final[,c("symbol_clean","fold","de","h1","k562")],"de_k562_h1.txt",quote=FALSE, row.names = FALSE)

