
class colunmTxt(object):
     def __init__(self,filename):
        self.lines = open(filename,'r').readlines()

     def getColunm(self,colunmNum):
        alist=[]
        alist = [line.strip().split()[colunmNum] for line in self.lines ]
        return alist

     def get_date(self,year,month,day,hour,minute):
        self.date=[]
        self.year=year
        self.month=month
        self.day=day
        self.hour=hour
        self.minute=minute

        a=len(self.year)
        for i in range(a):
            if self.minute[i]=='0':
                self.minute[i]='00'
            self.date.append(self.year[i]+"-"+self.month[i]+'-'+self.day[i]+'-'+self.hour[i]+':'+self.minute[i])
        return self.date

