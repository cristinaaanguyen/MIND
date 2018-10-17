.libPaths("F:/wpoon/cristina/R/win-library/3.4")
library(ggplot2)
library(ggrepel)


args = commandArgs(trailingOnly = TRUE)
res <- read.table(args[1], header=TRUE, sep = ",", row.names = 1)

png(paste(args[2],"\\" ,args[4], "volcanoplot_", args[3], ".png", sep = ""),
    width = 1500, height = 1500, units = "px")


res$threshold1 = as.factor(
  ifelse(res$pvalue < .01 & res$log2FoldChange > 1 & res$padj<.05, 1, ifelse(res$pvalue < .01 & res$log2FoldChange < -1 & res$padj<.05, -1, 0 )
  )) 

g = ggplot(data=res, aes(x=log2FoldChange, y=-log10(pvalue))) +
  geom_point(aes(colour = threshold1), size=5) +
  scale_colour_manual(values = c("0" = "gray", "1" = "red2", "-1" = "dodgerblue1")) +
  xlim(c(-10, 10)) + ylim(c(0, 150)) +
  xlab("log2 fold change") + ylab("-log10 FDR (vehicle)") + geom_text_repel(
    data = subset(res, padj < 0.0002 & (log2FoldChange > 1 | log2FoldChange < -1)), #padj has to be less than .001 AND if any of those conditions in the paranthesis are satisfied as well (log2FoldChange > 5 | log2FoldChange < -5 | -log10(pvalue) > 18) then label those points
    aes(label = selectgene),
    size = 9,box.padding = unit(0.35, "lines"),
    point.padding = unit(0.3, "lines")
   ) + scale_y_continuous (sec.axis = sec_axis(~.+0, name = "-log10 FDR (-TGFb)"))

 

g + theme(legend.position = "none", panel.background = element_rect(fill ="white", colour = "black"), text = element_text(size=60)) 

dev.off()

 