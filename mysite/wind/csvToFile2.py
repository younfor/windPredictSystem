# coding: utf-8
import csv


class csvToFile2(object):
    def __init__(self,filename):
        self.list=[]
        self.resultlist=[]
        for line in open(filename):
        	self.list.append(line.split());


    def get_list(self,column):
        self.resultlist=[]
        for content in self.list:
        	self.resultlist.append(content[column])
        return self.resultlist

    def get_date(self,year,month,day,hour,minute):
        self.date=[]
        self.year=year
        self.month=month
        self.day=day
        self.hour=hour
        self.minute=minute

        a=len(self.year)
	for i in range(a):
	    self.date.append(self.year[i]+"-"+self.month[i]+'-'+self.day[i]+'-'+self.hour[i]+':'+self.minute[i])

 	return self.date
