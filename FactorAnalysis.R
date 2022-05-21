#install packages
pkgs_CRAN <- c("lme4","MCMCglmm","blme",
               "MuMIn","coda","aods3","bbmle","ggplot2",
               "reshape2","dplyr","numDeriv","glmmADMB",
               "plotMCMC","gridExtra","R2admb",
               "broom.mixed","dotwhisker")
install.packages(pkgs_CRAN)

#import packages
library(ggplot2)
library(glmmADMB)
library(lme4)
library(MuMIn)
library(dplyr) 

#load data and transfer the data type
data<-read.csv("~/Documents/BigdataProcessing/crawler_beijing_property/complete_community_dataset.csv")
price<-as.numeric(data$price)
age<-as.numeric(as.integer(data$age))
dist_tam<-as.numeric(as.double(data$dist_tam))
cnt_school<-as.numeric(data$cnt_school)
cnt_subway<-as.numeric(as.integer(data$cnt_subway))
cnt_hospital<-as.numeric(as.integer(data$cnt_hospital))
cnt_mall<-as.numeric(as.integer(data$cnt_mall))
cnt_office<-as.numeric(as.integer(data$cnt_office))
region<-as.factor(data$dist)
year<-as.numeric(as.integer(data$year))

# run the GLMM 
models<- glmmadmb(price~age+dist_tam+cnt_subway+cnt_school+cnt_mall+cnt_office+cnt_hospital
                  +(cnt_office|region)
                  +(cnt_mall|region)
                  +(cnt_school|region),data=data,
                      family="gamma")
#plot the model result
summary(models)

# rank argument by AICc to select best model
select_feature=dredge(global.model = models,rank = "AICc") 
write.csv(select_feature,"../AIccResult.csv")

#plot the result of the analysis
suway=data %>% mutate(Interval=cut_width(data$cnt_subway, width =5, boundary = 0))
data$subway_interbal<-suway$Interval
subway_interbal<-as.factor(data$subway_interbal)

ggplot(data,aes(x=subway_interbal,y=price))+
  geom_point()+
  geom_boxplot()

hospdat=data %>% mutate(Interval=cut_width(data$cnt_hospital, width =2, boundary = 0))
data$hosp_interbal<-hospdat$Interval
hosp_interbal<-as.factor(data$hosp_interbal)

ggplot(data,aes(x=hosp_interbal,y=price))+
  geom_point()+
  geom_boxplot()

