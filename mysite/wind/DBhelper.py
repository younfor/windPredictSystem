from django.contrib.auth.models import User
from wind import models
from django.contrib import auth
import commands


class DBhelper:

    ins = None

    @staticmethod
    def getIns():
        if DBhelper.ins is None:
            return DBhelper()
        else:
            return DBhelper.ins

    def addPowerData(self, data):
        print 'save powerdata'
        data.save()

    def getScope(self, request):
        print 'get scope'
        scope = models.Factory.objects.get(user=request.user).scope
        print 'data,scope:', scope
        print 'decoding'
        scope = scope.split(':')
        s = []
        for sc in scope:
            s.append(sc.split(','))
        print s

    def getPlotWindByHeight(domain=1, height=1000, time=10):
        # out put wind_field-2013-01-03_11:30:00_dm1-1000m.png
        com1 = "cd /home/dwen/model/output/original/2013_01_30min_gn"
        print self.exeCommand(com1)
        com2 = "ncl dm=1 ht=1000 nt=10 extract_plot_wind_field_h.ncl"
        print self.exeCommand(com2)

    def getExtactWindSpeedByPoint(domain=4, height=68.5, lat=25.294600, lon=121.580935):
        # out put extr_dm4_wsp_at_25.29D121.58D68.50M.txt
        com1 = "cd /home/dwen/model/output/original/2013_01_30min_gn"
        print self.exeCommand(com1)
        com2 = "ncl dm=4 agh=68.5 lat=25.294600 lon=121.580935 extract_point_wind_timeseries.ncl"
        print self.exeCommand(com2)

    def getPlotWRF(domian=1):
        #out put WRF_map_dm1.png
        com1 = "cd /home/dwen/model/output/original/2013_01_30min_gn"
        print self.exeCommand(com1)
        com2 = "ncl dm=1 wrf_map.ncl"
        print self.exeCommand(com2)

    def exeCommand(args):
        commands.getoutput(args)
