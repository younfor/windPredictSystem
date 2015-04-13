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

    def exeCommand(args):
        commands.getoutput(args)
