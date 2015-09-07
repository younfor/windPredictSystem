from django.contrib.auth.models import User
from wind import models
from django.contrib import auth
import commands
import thread
# thread function

COMMPATH = "/E/dwen/model/output/original/china_lat-5.01lon81.43_lat33.23lon174.14-2013-feb/"
PATH = "cd /E/dwen/model/output/original"
'''
for dm=1
lat=2.5000N--44.0000N   
lon=81.0000E--147.0000E
for dm=2
lat=10.5000N--33.5000N   
lon=109.5000E--131.1000E  
for dm=3
lat=20.1000N--27.2000N
lon=117.3000E--123.6000E
for dm=4
lat=23.2000N--26.5000N 
lon=120.1500E--122.2200E
'''


def getDate(dt='2015/08/04 22:32'):
    return dt[0:4] + '-' + dt[5:7] + '-' + dt[8:10] + '_' + dt[11:] + ':00'


def getPlotWindByHeight(dm=1, ht=200.5, dt="2013-02-04_12:30:00"):
    # out put wind_field-2013-01-03_11:30:00_dm1-1000m.png
    global COMMPATH
    global PATH
    dt = getDate(dt)
    com = '''ncl dm=''' + dm + ''' 'dir="''' + COMMPATH + \
        '''"' ht=''' + ht + ''' 'dt="''' + dt + \
        '''"'  extract_wind_stream_field_h.ncl'''
    print 'cmd is :', com
    print commands.getoutput(PATH + " && " + com)
    print 'finish getPlotWindByHeight'
    

def getExtactWindSpeedByPoint(dm=1, agh=68.5, lat=25.294600, lon=121.580935, st="2013-02-04_12:30:00", et="2013-02-07_01:00:00"):
    # out put extr_dm4_wsp_at_25.29D121.58D68.50M.txt
    global COMMPATH
    global PATH
    print 'start extact'
    st = getDate(st)
    et = getDate(et)
    print st
    print et
    com = '''ncl dm=1 'dir="''' + COMMPATH + \
        '''"' agh=68.5 lat=''' + lat + ''' lon=''' + lon + ''' 'st="''' + st + \
        '''"' 'et="''' + et + '''"' extract_point_wind_timeseries.ncl'''
    # com = '''ncl dm=''' + dm + '''   lat=''' + lat + ''' lon=''' + lon + ''' 'st="''' + st + \
    #     '''"' 'et="''' + et + '''"' extract_point_wind_timeseries.ncl'''
    print 'cmd is :', com
    print commands.getoutput(PATH + " && " + com)
    print 'finish getExtactWindSpeedByPoint'


def getPlotWRF(dm=1):
    # out put WRF_map_dm1.png
    global COMMPATH
    global PATH
    com = '''ncl 'dir="''' + COMMPATH + '''"' dm=''' + dm + ''' wrf_map.ncl'''
    print 'cmd is :', com
    print commands.getoutput(PATH + " && " + com)
    print 'finish getPlotWRF'
# class provide data for ncl


class CmdExec:

    ins = None

    @staticmethod
    def getIns():
        if CmdExec.ins is None:
            return CmdExec()
        else:
            return CmdExec.ins

    def execCmd(self, tag, *data):
        print 'tag:', tag, data
        if tag == 0:
           # thread.start_new_thread(
            getPlotWindByHeight(data[0], data[1], data[2])  # )
        if tag == 1:
            getExtactWindSpeedByPoint(
                data[0], data[1], data[2], data[3], data[4], data[5])
        if tag == 2:
            # thread.start_new_thread(
            getPlotWRF(data[0])  # )
