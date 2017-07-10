
#biocLite("illuminaHumanv4.db","limma")
library("beadarray")
library("illuminaHumanv4.db")
library("limma")

library(RColorBrewer)

hmcol <- colorRampPalette(brewer.pal(9, "Reds"))(256)
hmcol <- hmcol[length(hmcol):1]


f=read.table("files.txt")
data=readIdatFiles(idatFiles=as.character(f[,1]))

data_final=exprs(data)

data_final=normalizeBetweenArrays(log2(data_final+1))

info=readSampleSheet("sampleSheet.csv")

x=info$sampleSheet

design <- model.matrix(~ 0+factor(c(1,2,3,4,1,2,3,4,1,2,5,3)))
colnames(design) <- c("Con","LPS_n","n_LPS","LPS_LPS","aux")

fit <- lmFit(data_final, design)
contrast.matrix <- makeContrasts(LPS_n-Con,LPS_LPS-LPS_n, levels=design)
fit2 <- contrasts.fit(fit, contrast.matrix)
fit2 <- eBayes(fit2)


colnames(data_final)=info$sampleSheet[,4]
#data_final=data_final[,-11]
#pdf("heatmap.pdf")
#heatmap.2(as.matrix(dist(t(data_final))),trace="none", col=hmcol,margins = c(9,9))
#dev.off()

results_05 <- decideTests(fit2,lfc=1)

pdf("Venn.pdf")
vennDiagram(results_05)
dev.off()


ids=data.frame(Gene=unlist(mget(x =rownames(data_final),envir = illuminaHumanv4SYMBOL)))


final=as.data.frame(results_05)
final=merge(ids,final,by="row.names")

write.table(final[final[,3]==1,"Gene"],"LPS_n_UP.txt",quote=FALSE, row.names = FALSE)
write.table(final[final[,3]==-1,"Gene"],"LPS_n_DOWN.txt",quote=FALSE, row.names = FALSE)
#write.table(final[final[,4]==1,"Gene"],"n_LPS_UP.txt",quote=FALSE, row.names = FALSE)
#write.table(final[final[,4]==-1,"Gene"],"n_LPS_DOWN.txt",quote=FALSE, row.names = FALSE)
#write.table(final[final[,5]==1,"Gene"],"LPS_LPS_UP.txt",quote=FALSE, row.names = FALSE)
#write.table(final[final[,5]==-1,"Gene"],"LPS_LPS_DOWN.txt",quote=FALSE, row.names = FALSE)
write.table(final[final[,4]==1,"Gene"],"LPS_LPS_LPS_n_UP.txt",quote=FALSE, row.names = FALSE)
write.table(final[final[,4]==-1,"Gene"],"LPS_LPS_LPS_n_DOWN.txt",quote=FALSE, row.names = FALSE)


