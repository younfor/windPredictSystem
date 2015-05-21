

library(nnet)

data1=read.table("T6 NWP.txt" )

data2=read.table("T6 EXP.txt")

x1=data1[,1]

x2=data2[,1]


length(x1)

length(x2)

#x2=2*x2;
#df=data.frame(cbind(x1, x2))


rep1=30 # number of ensemble components

nn=240 # sample size if training data

nn2=384-nn  #nn2=84
nn_bootstrap=sample(1:nn, nn,replace=T) ##a sequence for extracting training data from the whole data set

nn1=seq(1:nn)

df=cbind(data1,data2)

colnames(df)=c("y1","y2")

number=rep1*nn2

predict1_out=matrix(seq(1:number), ncol=nn2) # the whole matrix for the out-of-sample prediction

number=rep1*nn

predict1_in=matrix(seq(1:number), ncol=nn) # the whole matrix for the in-sample-prediction

cheese1=df[nn_bootstrap,]

#data_train=df[nn_bootstrap,]

nnfit<-nnet(y2~y1, data=cheese1, size=6,skip=F,trace=F, decay = 5e-4,maxit = 1000,linout=TRUE)





# data_=df[nn1,]

# cheese2=cheese[-nn,c(3,4,5)]

# data_pred_in=matrix(c(12.9, 13.4, 23,25), nrow=2)

# dd=data.frame(data_pred_in)
# 
# colnames(dd)=c("y1")
# 
# y.fit=predict(nnfit, dd)
# 




data_pred_in=df[nn1,1]

data_pred_in=data.frame(data_pred_in)

colnames(data_pred_in)=c("y1")

y.fit=predict(nnfit, data_pred_in)


# y.fit=predict(nnfit, predict1_in)
# 

write.table(matrix(y.fit, ncol=length(y.fit)), "wind prediction in.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)

data_pred_out=df[-nn1,1]

data_pred_out=data.frame(data_pred_out)

colnames(data_pred_out)=c("y1")

# 
# is.data.frame(data_pred_out)

y.fit1=predict(nnfit, data_pred_out)


write.table(matrix(y.fit1, ncol=length(y.fit1)), "wind prediction_out.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)


# net.results_out1=net.results_out



#par(mfrow=c(2,1))

#plot(data2[-nn,], type="l", col="blue"  )

#lines(net.results_out1$net.result, col="red", ylim=c(min(data2$exp[-nn], net.results_out1$net.result)-1,1+ max(data2$exp[-nn], net.results_out$net.result)) , xlim=c(1, nn2)  )



numb=1
predict1_in[numb,]=matrix(y.fit, ncol=length(y.fit))

predict1_out[numb,]=matrix(y.fit1, ncol=length(y.fit1))

for( j in(1:5))

{
  
mm=rep1+5

for (i in (7:mm))
  
  
  
{
  
  nn_bootstrap=sample(1:nn, nn,replace = TRUE) ##a sequence for extracting training data from the whole data set
  
  data_train=df[nn_bootstrap,]
  
  print (i)
  
  nnfit<-nnet(y2~y1, data=data_train, size=i,skip=F,decay = 5e-4, trace=F,maxit=1000,linout=TRUE)
  
  
  # data_pred_in=df[nn1,]
  #  data_pred_in=df[nn1,c(1)]
  #  
  
  y.fit=predict(nnfit, data_pred_in)
  
  
  write.table(matrix(y.fit, ncol=length(y.fit)), "wind prediction in.csv",append = T, sep=",", row.names=FALSE,  col.names=FALSE)
  
  #   data_pred_out=df[-nn1,]
  
  
  
  
  y.fit1=predict(nnfit, data_pred_out)
  
  
  write.table(matrix(y.fit1, ncol=length(y.fit1)), "wind prediction_out.csv",append = T, sep=",", row.names=FALSE,  col.names=FALSE)
  
  
  # net.results_out1=net.results_out
  
  
  
  #par(mfrow=c(2,1))
  
  #plot(data2[-nn,], type="l", col="blue"  )
  
  #lines(net.results_out1$net.result, col="red", ylim=c(min(data2$exp[-nn], net.results_out1$net.result)-1,1+ max(data2$exp[-nn], net.results_out$net.result)) , xlim=c(1, nn2)  )
  
  numb=i-5
  
  predict1_in[numb,]=matrix(y.fit, ncol=length(y.fit))
  
  predict1_out[numb,]=matrix(y.fit1, ncol=length(y.fit1))
  
  
  
}
}

nn1=seq(1:nn)
y1_in=x2[1:nn]
y1_out=x2[(nn+1):384]



 par(mfrow=c(2,2))




pred_ave_in=colMeans(predict1_in)
pred_ave_out=colMeans(predict1_out)

write.table(matrix(pred_ave_out, ncol=length(pred_ave_out)), "wind prediction_out_ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)

write.table(matrix(pred_ave_in, ncol=length(pred_ave_in)), "wind prediction_in_ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)



library(matrixStats)

predict_in_var=colVars(predict1_in)
predict_in_std=colSds(predict1_in)



predict_in_std_high=pred_ave_in +predict_in_std*1.96

predict_in_std_low =pred_ave_in -predict_in_std*1.96

write.table(matrix(predict_in_std_high, ncol=length(predict_in_std_high)), "wind prediction_in_ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)

write.table(matrix(predict_in_std_low, ncol=length(predict_in_std_low)), "wind prediction_in_ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)


predict_out_var=colVars(predict1_out)
predict_out_std=colSds(predict1_out)


predict_out_std_high=pred_ave_out +predict_out_std*1.96

predict_out_std_low=pred_ave_out -predict_out_std*1.96

write.table(matrix(predict_out_std_high, ncol=length(predict_out_std_high)), "wind prediction_out_ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)

write.table(matrix(predict_out_std_high, ncol=length(predict_out_std_high)), "wind prediction_out_ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)




ylim_low= min(data2$V1[nn1], y1_out,predict_out_std_low)-1

ylim_high= max(data2$V1[nn1],y1_out,predict_out_std_high)+1



nn1_out=seq(1:nn2)

plot(nn1_out,y1_out,type="l", col="blue" ,lwd = 2,ylim=c(ylim_low, ylim_high), ylab="Wind speed" , xlab="Hour", col.lab="blue" )


title(main = "Out-of-sample prediction (simple mean)", col.main="red")

lines(pred_ave_out, col="red",lwd = 2 )

lines(predict_out_std_low, col="green",lwd = 2 )

lines(predict_out_std_high, col="green",lwd = 2)


pdf("out ofsample mean.pdf")

plot(nn1_out,y1_out,type="l", col="blue" ,lwd = 2,ylim=c(ylim_low, ylim_high), ylab="Wind speed" , xlab="Hour", col.lab="blue" )


title(main = "Out-of-sample prediction (simple mean)", col.main="red")

lines(pred_ave_out, col="red",lwd = 2 )

lines(predict_out_std_low, col="green",lwd = 2 )

lines(predict_out_std_high, col="green",lwd = 2)

dev.off()



#pred_ave_in=colMeans(predict1_in)

ylim_low= min(data2$V1[nn1], y1_in,predict_in_std_low)-1

ylim_high= max(data2$V1[nn1],y1_in,predict_in_std_high)+1



plot(nn1,y1_in,  ylim=c(ylim_low, ylim_high) , xlim=c(1, nn), type="l", col="blue", lwd = 2 ,ylab="Wind speed" , xlab="Hour", col.lab="blue" )



title(main = "In-sample prediction (simple mean)",col.main="red")

lines(pred_ave_in, col="red",lwd = 2   )


lines(predict_in_std_low, col="green",lwd = 2  )

lines(predict_in_std_high, col="green",lwd = 2)


pdf("in sample simple mean.pdf")

plot(nn1,y1_in,  ylim=c(ylim_low, ylim_high) , xlim=c(1, nn), type="l", col="blue", lwd = 2 ,ylab="Wind speed" , xlab="Hour", col.lab="blue" )



title(main = "In-sample prediction (simple mean)",col.main="red")

lines(pred_ave_in, col="red",lwd = 2   )


lines(predict_in_std_low, col="green",lwd = 2  )

lines(predict_in_std_high, col="green",lwd = 2)

dev.off()



# pred_ave_in=colMeans(predict1_in)
# pred_ave_out=colMeans(predict1_out)
# 
# write.table(matrix(pred_ave_out, ncol=length(pred_ave_out)), "wind prediction_out_weight ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)
# 
# write.table(matrix(pred_ave_in, ncol=length(pred_ave_in)), "wind prediction_in_weight ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)
# 


mean_matrix_in=t(matrix(rep(pred_ave_in, rep1), nrow=nn))


temp=(predict1_in-mean_matrix_in)

P=temp%*%t(temp)+diag(rep1)


library(quadprog)



d=matrix(0, nrow=1, ncol=rep1)

A=diag(rep1)

a1=matrix(1, nrow=rep1)
A=cbind(a1, A)

b=matrix(0, ncol=rep1+1)
b[1]=1

sol = solve.QP (P, -d, A, b,meq=1)

weight=sol$solution



pred_out_ave=weight%*%predict1_out


pred_in_ave=weight%*%predict1_in

write.table(matrix(pred_ave_out, ncol=length(pred_ave_out)), "wind prediction_out_weight ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)

write.table(matrix(pred_ave_in, ncol=length(pred_ave_in)), "wind prediction_in_weight ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)



# calculate confidence intervals




predict_out_matrix=t(matrix(rep(pred_out_ave[1,],rep1),nrow=nn2, ncol=rep1))

predict_out_std=sqrt( weight%*%(predict_out_matrix-predict1_out)^2/(1-sum(weight^2)))

predict_out_std_high=pred_out_ave[1,] +predict_out_std[1,]*1.96

predict_out_std_low=pred_out_ave[1,] -predict_out_std[1,]*1.96


write.table(matrix(predict_out_std_high, ncol=length(predict_out_std_high)), "wind prediction_out_weight ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)

write.table(matrix(predict_out_std_high, ncol=length(predict_out_std_high)), "wind prediction_out_weight ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)


ylim_low= min( data2[-nn1,],predict_out_std_low)-1

ylim_high= max(data2[-nn1,],predict_out_std_high)+1


plot(nn1_out, data2[-nn1,], ylim=c(ylim_low, ylim_high) , xlim=c(1, nn2),type="l", col="blue" ,lwd = 2 ,ylab="Wind speed" , xlab="Hour", col.lab="blue")
title(main = "Out-of-sample prediction (weighted mean)",col.main="red")


lines(pred_out_ave[1,], col="red",lwd = 2   )

lines(predict_out_std_low, lwd=2, col="green")

lines(predict_out_std_high, lwd=2,col="green")

pdf("out of sample weighted mean.pdf")

plot(nn1_out, data2[-nn1,], ylim=c(ylim_low, ylim_high) , xlim=c(1, nn2),type="l", col="blue" ,lwd = 2 ,ylab="Wind speed" , xlab="Hour", col.lab="blue")
title(main = "Out-of-sample prediction (weighted mean)",col.main="red")


lines(pred_out_ave[1,], col="red",lwd = 2   )

lines(predict_out_std_low, lwd=2, col="green")

lines(predict_out_std_high, lwd=2,col="green")


dev.off()

predict_in_matrix=t(matrix(rep(pred_in_ave[1,],rep1),nrow=nn, ncol=rep1))

predict_in_std=sqrt( weight%*%(predict_in_matrix-predict1_in)^2/(1-sum(weight^2)))




ylim_low= min( data2[nn1,],predict_in_std_low)-1

ylim_high= max(data2[nn1,],predict_in_std_high)+1


predict_in_std_high=pred_in_ave[1,] +predict_in_std[1,]*1.96

predict_in_std_low=pred_in_ave[1,] -predict_in_std[1,]*1.96

write.table(matrix(predict_in_std_high, ncol=length(predict_in_std_high)), "wind prediction_in_weight ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)

write.table(matrix(predict_in_std_low, ncol=length(predict_in_std_low)), "wind prediction_in_weight ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)





plot(nn1, data2[nn1,], ylim=c(ylim_low, ylim_high) , xlim=c(1, nn), type="l", col="blue", lwd = 2 ,ylab="Wind speed" , xlab="Hour", col.lab="blue")
title(main = "In-sample prediction (weighted mean)",col.main="red")



lines(pred_in_ave[1,], col="red",lwd = 2)



lines(predict_in_std_low, col="green",lwd = 2)

lines(predict_in_std_high, col="green",lwd = 2)



pdf("in sample weighted mean.pdf")


plot(nn1, data2[nn1,], ylim=c(ylim_low, ylim_high) , xlim=c(1, nn), type="l", col="blue", lwd = 2 ,ylab="Wind speed" , xlab="Hour", col.lab="blue")
title(main = "In-sample prediction (weighted mean)",col.main="red")



lines(pred_in_ave[1,], col="red",lwd = 2)



lines(predict_in_std_low, col="green",lwd = 2)

lines(predict_in_std_high, col="green",lwd = 2)
dev.off()

# 
# 
# pred_in=weight%*%predict1_in
# plot(data2[nn1,], type="l", col="blue", lwd = 2 ,ylab="Wind speed" , xlab="Hour", col.lab="blue",cex.lab=1.5  )
# title(main = "In sample prediction",col.main="red",cex.main= 1.5)
# 
# lines(pred_in[1,], col="red",lwd = 2 ,  ylim=c(min(data2$exp[nn], pred_in[1,])-1,1+ max(data2$exp[nn],pred_in) , xlim=c(1, 300)  ))
# 
# 
# 
# lines(predict_in_std_low, col="green",lwd = 2 ,  ylim=c(min(data2$exp[nn], pred_in[1,])-1,1+ max(data2$exp[nn],pred_in) , xlim=c(1, 300)  ))
# 
# lines(predict_in_std_high, col="green",lwd = 2 ,  ylim=c(min(data2$exp[nn], pred_in[1,])-1,1+ max(data2$exp[nn],pred_in) , xlim=c(1, 300)  ))
# 




#library(matrixStats)
#predict_in_var=colVars(predict1_in)
#predict_in_std=sqrt()
