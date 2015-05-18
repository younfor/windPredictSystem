class txt_file(object):
    #def __init__(self):
    # row means how many cols 
    def __init__(self,filename,row):
       f=open(filename)
       self.l=[]
       self.chartlist=[]
       s=f.readline()
       while s!='':
            arr=s.split()
            self.l=self.l+arr
            s=f.readline()
            # print a1
            # print len(a1)
       length=len(self.l)/row
       self.list=[[]*row]*length
       for j in range(length):
            self.list[j]=self.l[6*j:6*j+row]
            j=j+1
     #############get table data#################

     ################get chart data##############
       # self.chartlist=[[]*length]*row
       #    lines = open(filename,'r').readlines()
       #    self.chartlist[j] = [line.strip().split()[j] for line in lines ]
       #    j=j+1

    def get_list(self):
         print self.list[22] 
         return self.list
    # def get_chartlist(self,num):
    #      print self.chartlist[num]
    #      return self.chartlist[num]
    #num means which col to read
    def get_chartlist(self,num):
        self.chartlist=zip(*self.list)
        # print self.chartlist[5] 
        return self.chartlist[num]