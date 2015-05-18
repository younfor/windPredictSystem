# coding: utf-8
import csv
class txtNotAll(object):
    def __init__(self,filename,fromnum,tonum):
        i=0
        self.list=[]
        txtfile = file(filename, 'rb')
        for line in txtfile:
             i=i+1
             if i>fromnum and i<=tonum:
                a=line.split()
                b=a[0]
                self.list.append(b)
        print len(self.list)
        txtfile.close()
    def get_list(self):
        return self.list
