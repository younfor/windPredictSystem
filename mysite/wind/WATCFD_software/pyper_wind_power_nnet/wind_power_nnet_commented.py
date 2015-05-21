#import pandas as pd
# 
#import statsmodels.api as sm
# 
#data = pd.read_table('csdata1.txt')
# 
##Y = data.gpa
# 
#X = sm.add_constant(data[['COLLAT1', 'SIZE1', 'PROF2', 'LIQ', 'IND3A']])
# 
## Discrete Dependent Variable Models with Logit Link
# 
#mod = sm.Logit(Y, X)
# 
#res = mod.fit()

# load the package PypeR, which we use to call functions and packages such as nnet from within Python. 
# Through PyperR we Python and R can communicate.  
#
import pyper as pr

# we will use numerical Python for numerical value manipulation. 
import numpy as np

# Pandas will be used for data processing when calling R from Python 
r = pr.R(use_pandas = True)
 
#r.r_data = data

#r('data <- rbind(r_data, y = 1, wt = r_data$LEV_LT3), cbind(r_data, y = 0, wt = 1 - r_data$LEV_LT3))')


# r('mod <- lm(gpa ~ ., data = data)')


#load everyting in PyperR 
from pyper import *


#outputs = r("x1=seq(1,50, 1); x2=seq(1,100,2); d <- data.frame(x1,x2)")
#print(outputs)

# load R package, nnet, which is the package that is called to train our artificial neural networks (ANNs)
outputs1 = r("library(nnet)")

# laod the input data for ANN training
r("data1 <- read.table('T6 NWP.txt' )")

# load the output data fore ANN training
r("data2 <- read.table('T6 power.txt' )")

# The number of ensmeble ANNs 
r("rep1=30")

# sample size of the training data
r("nn=240")

# same size of the assessment data. that means we have 144 observations for model (or forecasting assessment)
r("nn2=384-nn")

# we do bootstrapping 
r("nn_bootstrap=sample(1:nn, nn,replace=T)")

# make a dataframe for nnet to use
r("nn1=seq(1:nn);\
df=cbind(data1,data2);\
colnames(df)=c('y1','y2');\
number=rep1*nn2")

# two matrices to store in-sample and out-of-sample predicted values; Cheese1 is the dataframe for nnet training 
r("predict1_out=matrix(seq(1:number), ncol=nn2);\
number=rep1*nn;\
predict1_in=matrix(seq(1:number), ncol=nn);\
cheese1=df[nn_bootstrap,]")

# ANN training for the first ensemble ANN
r("nnfit<-nnet(y2~y1, data=cheese1, size=6,skip=F,maxit=50000,decay = 5e-4,linout=TRUE)")

# perform in-sample and out-of-sample predictions (forecasting)
r("data_pred_in=df[nn1,1];\
data_pred_in=data.frame(data_pred_in);\
colnames(data_pred_in)=c('y1');\
y.fit=predict(nnfit, data_pred_in)")

# save the in-sample predictions
r("write.table(matrix(y.fit, ncol=length(y.fit)), 'wind prediction in.csv',append = FALSE, sep=',', row.names=FALSE,  col.names=FALSE)")


# prepare data for out-of-sample forecasting
r("data_pred_out=df[-nn1,1]")

r("data_pred_out=data.frame(data_pred_out)")

r("colnames(data_pred_out)=c('y1')")


# make out-of-sample prediction 
r("y.fit1=predict(nnfit, data_pred_out)")

# save out-of-sample predicted values
r("write.table(matrix(y.fit1, ncol=length(y.fit1)), 'wind prediction_out.csv',append = FALSE, sep=',', row.names=FALSE,  col.names=FALSE)")





#r("traininginput <-  as.data.frame(traininginput1)")
#
#
#r("trainingoutput <- sqrt(traininginput)")
#
#r('write.table(t(traininginput1), "export1.example.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')
#


# save the predicted values
r("numb=1")
r("predict1_in[numb,]=matrix(y.fit, ncol=length(y.fit))")

r("predict1_out[numb,]=matrix(y.fit1, ncol=length(y.fit1))")

## mm is  35
r("mm=rep1+5")

# train ensemble ANNs 
r('for (j in (1:5))\
  {for (i in (7:mm))\
  {\
   nn_bootstrap=sample(1:nn, nn);\
   data_train=df[nn_bootstrap,];\
   print (i);\
   nnfit<-nnet(y2~y1, data=data_train, size=i,skip=F,decay = 5e-4,maxit=50000, linout=TRUE);\
   y.fit=predict(nnfit, data_pred_in);\
   write.table(matrix(y.fit, ncol=length(y.fit)), "wind prediction in.csv",append = T, sep=",", row.names=FALSE,  col.names=FALSE);\
   y.fit1=predict(nnfit, data_pred_out);\
   write.table(matrix(y.fit1, ncol=length(y.fit1)), "wind prediction_out.csv",append = T, sep=",", row.names=FALSE,  col.names=FALSE);\
   numb=i-5;\
   predict1_in[numb,]=matrix(y.fit, ncol=length(y.fit));\
   predict1_out[numb,]=matrix(y.fit1, ncol=length(y.fit1))\
   }\
   }\
   ')
# end of the training process


# prepare data
r("nn1=seq(1:nn); y1_in=x2[1:nn];y1_out=x2[245:384]")

#r("par(mfrow=c(2,2))")

# calculate averages of predictions
r("pred_ave_in=colMeans(predict1_in)")
r("pred_ave_out=colMeans(predict1_out)")

# save predicted means
r('write.table(matrix(pred_ave_out, ncol=length(pred_ave_out)), "wind prediction_out_ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

r('write.table(matrix(pred_ave_in, ncol=length(pred_ave_in)), "wind prediction_in_ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

# load a package for matrix means and variances
r('library(matrixStats)')

# calculate simple means and standard deviations
r("predict_in_var=colVars(predict1_in)")
r("predict_in_std=colSds(predict1_in)")

#calcuate confidence intervals of the the in-sample predictions
r("predict_in_std_high=pred_ave_in +predict_in_std*1.96")

r("predict_in_std_low =pred_ave_in -predict_in_std*1.96")


# save the confidence intervals
r('write.table(matrix(predict_in_std_high, ncol=length(predict_in_std_high)), "wind prediction_in_ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

r('write.table(matrix(predict_in_std_low, ncol=length(predict_in_std_low)), "wind prediction_in_ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')


# calculate simple means and standard deviations
r("predict_out_var=colVars(predict1_out)")
r("predict_out_std=colSds(predict1_out)")

#calcuate confidence intervals of the out-of-sample predictions
r("predict_out_std_high=pred_ave_out +predict_out_std*1.96")

r("predict_out_std_low=pred_ave_out -predict_out_std*1.96")



# save the confidence intervals
r('write.table(matrix(predict_out_std_high, ncol=length(predict_out_std_high)), "wind prediction_out_ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

r('write.table(matrix(predict_out_std_low, ncol=length(predict_out_std_high)), "wind prediction_out_ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')


# prepare data for calculating weights
r("mean_matrix_in=t(matrix(rep(pred_ave_in, rep1), nrow=nn))")


r("temp=(predict1_in-mean_matrix_in)")

r("P=temp%*%t(temp)+diag(rep1)")


#load a package to solve a quadratic optimization problem
r("library(quadprog)")


# solve a contrained optimization problem to obtain the weights
r("d=matrix(0, nrow=1, ncol=rep1)")

r("A=diag(rep1)")

r("a1=matrix(1, nrow=rep1)")
r("A=cbind(a1, A)")

r("b=matrix(0, ncol=rep1+1)")
r("b[1]=1")

r("sol = solve.QP (P, -d, A, b,meq=1)")

r("weight=sol$solution")


# calculate weighted means

r("pred_out_ave=weight%*%predict1_out")


r("pred_in_ave=weight%*%predict1_in")

# write the resultes to files

r('write.table(matrix(pred_ave_out, ncol=length(pred_ave_out)), "wind prediction_out_weight ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

r('write.table(matrix(pred_ave_in, ncol=length(pred_ave_in)), "wind prediction_in_weight ave.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')


# calculate the standard deviateions
r("predict_out_matrix=t(matrix(rep(pred_out_ave[1,],rep1),nrow=nn2, ncol=rep1))")

r("predict_out_std=sqrt( weight%*%(predict_out_matrix-predict1_out)^2/(1-sum(weight^2)))")

# calculate confidence intervals

r("predict_out_std_high=pred_out_ave[1,] +predict_out_std[1,]*1.96")

r("predict_out_std_low=pred_out_ave[1,] -predict_out_std[1,]*1.96")

# write confidence interval to files
r('write.table(matrix(predict_out_std_high, ncol=length(predict_out_std_high)), "wind prediction_out_weight ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

r('write.table(matrix(predict_out_std_low, ncol=length(predict_out_std_high)), "wind prediction_out_weight ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')


#calculate standard deviations
r("predict_in_matrix=t(matrix(rep(pred_in_ave[1,],rep1),nrow=nn, ncol=rep1))")

r("predict_in_std=sqrt( weight%*%(predict_in_matrix-predict1_in)^2/(1-sum(weight^2)))")

#calculate confidence intervals
r("predict_in_std_high=pred_in_ave[1,] +predict_in_std[1,]*1.96")

r("predict_in_std_low=pred_in_ave[1,] -predict_in_std[1,]*1.96")


# wriate confidence intervals to files
r('write.table(matrix(predict_in_std_high, ncol=length(predict_in_std_high)), "wind prediction_in_weight ave high.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')

r('write.table(matrix(predict_in_std_low, ncol=length(predict_in_std_low)), "wind prediction_in_weight ave low.csv",append = FALSE, sep=",", row.names=FALSE,  col.names=FALSE)')









# we now come to Python codes to plot our results



##   read and plot ------------------------------------

# load pandas package
import pandas as pd

#load numpy package
import numpy as np

# load package for plotting
import matplotlib.pyplot as plt

# load package to same graphics to pdf files
from matplotlib.backends.backend_pdf import PdfPages

# sample size of the training set
nn=240

# sample size for the set used for model assessment 
nn2=384-nn

# laod experiment data 
exp_data = np.loadtxt('T6 power.txt')


# plot the the in-sample equally weighted predictions with confidence intervals to a pdf file and on the screen

pp = PdfPages("In-sample equal weight prediction.pdf")
plt.figure (1)
plt.clf()
plt.plot(exp_data[0:nn],label="EXP")


exp_in_average= np.loadtxt(open("wind prediction_in_ave.csv","rb"),delimiter=",")

plt.plot(exp_in_average,color="red", linewidth=1.0, linestyle="-", label="Average")


exp_in_average_low= np.loadtxt(open("wind prediction_in_ave low.csv","rb"),delimiter=",")

exp_in_average_high= np.loadtxt(open("wind prediction_in_ave high.csv","rb"),delimiter=",")

plt.plot(exp_in_average_low,color="green", linewidth=2.0, linestyle="--",label="Confidence interval")
plt.plot(exp_in_average_high,color="green", linewidth=2.0, linestyle="--")
#c=np.concatenate((a,b))
plt.ylim(min(np.concatenate((exp_data[0:nn],exp_in_average_low), axis=1))-50, max(np.concatenate((exp_data[0:nn],exp_in_average_high), axis=1))+50)

plt.xlim(1,nn)

plt.legend(loc='upper right')

plt.ylabel('Wind speed', fontsize=28)
plt.xlabel('Hour', fontsize=28)

plt.title('In-sample equal weight prediction', fontsize=28)

pp.savefig()
pp.close()




# plot the the out-of-sample equally weighted predictions with confidence intervals to a pdf file and on the screen


pp = PdfPages("Out-of-sample equal weight prediction.pdf")
plt.figure (2)
plt.clf()
plt.plot(exp_data[(nn+1):384],label="EXP")

plt.ylim(min(np.concatenate((exp_data[(nn+1):384],exp_in_average_low), axis=1))-50, max(np.concatenate((exp_data[(nn+1):384],exp_in_average_high), axis=1))+50)

plt.xlim(1,nn2)

exp_out_average= np.loadtxt(open("wind prediction_out_ave.csv","rb"),delimiter=",")

plt.plot(exp_out_average,color="red", linewidth=1.0, linestyle="-", label="Average")


exp_out_average_low= np.loadtxt(open("wind prediction_out_ave low.csv","rb"),delimiter=",")

exp_out_average_high= np.loadtxt(open("wind prediction_out_ave high.csv","rb"),delimiter=",")

plt.plot(exp_out_average_low,color="green", linewidth=2.0, linestyle="--",label="Confidence interval")
plt.plot(exp_out_average_high,color="green", linewidth=2.0, linestyle="--")
#c=np.concatenate((a,b))

plt.legend(loc='upper left')



plt.ylabel('Wind speed', fontsize=28)
plt.xlabel('Hour', fontsize=28)

plt.title('Out-of-sample equal weight prediction', fontsize=28)
pp.savefig()
pp.close()


# plot the the in-sample weighted predictions with confidence intervals to a pdf file and on the screen


pp = PdfPages("In-sample weighted prediction.pdf")
plt.figure (3)
plt.clf()
plt.plot(exp_data[0:nn],label="EXP")


exp_in_average= np.loadtxt(open("wind prediction_in_weight ave.csv","rb"),delimiter=",")

plt.plot(exp_in_average,color="red", linewidth=1.0, linestyle="-", label="Average")


exp_in_average_low= np.loadtxt(open("wind prediction_in_weight ave low.csv","rb"),delimiter=",")

exp_in_average_high= np.loadtxt(open("wind prediction_in_weight ave high.csv","rb"),delimiter=",")

plt.plot(exp_in_average_low,color="green", linewidth=2.0, linestyle="--",label="Confidence interval")
plt.plot(exp_in_average_high,color="green", linewidth=2.0, linestyle="--")
#c=np.concatenate((a,b))
plt.ylim(min(np.concatenate((exp_data[0:nn],exp_in_average_low), axis=1))-50, max(np.concatenate((exp_data[0:nn],exp_in_average_high), axis=1))+50)



plt.xlim(1,nn)

plt.legend(loc='upper right')

plt.title('In-sample weighted prediction', fontsize=28)
plt.ylabel('Wind speed', fontsize=28)
plt.xlabel('Hour', fontsize=28)
pp.savefig()
pp.close()

# plot the the out-of-sample weighted predictions with confidence intervals to a pdf file and on the screen


pp = PdfPages("Out-of-sample equal weighted prediction.pdf")
plt.figure (4)
plt.clf()
plt.plot(exp_data[(nn+1):384],label="EXP")

plt.ylim(min(np.concatenate((exp_data[(nn+1):384],exp_in_average_low), axis=1))-50, max(np.concatenate((exp_data[(nn+1):384],exp_in_average_high), axis=1))+50)



plt.xlim(1,nn2)

exp_out_average= np.loadtxt(open("wind prediction_out_weight ave.csv","rb"),delimiter=",")

plt.plot(exp_out_average,color="red", linewidth=1.0, linestyle="-", label="Average")


exp_out_average_low= np.loadtxt(open("wind prediction_out_weight ave low.csv","rb"),delimiter=",")

exp_out_average_high= np.loadtxt(open("wind prediction_out_weight ave high.csv","rb"),delimiter=",")

plt.plot(exp_out_average_low,color="green", linewidth=2.0, linestyle="--",label="Confidence interval")
plt.plot(exp_out_average_high,color="green", linewidth=2.0, linestyle="--")
#c=np.concatenate((a,b))

plt.legend(loc='upper left')

plt.title('Out-of-sample equal weighted prediction', fontsize=28)

plt.ylabel('Wind speed', fontsize=28)
plt.xlabel('Hour', fontsize=28)

pp.savefig()
pp.close()










