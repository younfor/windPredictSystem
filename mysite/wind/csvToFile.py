# coding: utf-8
import csv


class csvToFile(object):
    def __init__(self,filename):
        csvfile = file(filename, 'rb')
        reader = csv.reader(csvfile)
        for line in reader:
            self.list=line
        csvfile.close() 

    def get_list(self):
        return self.list
