from django.contrib.auth.models import User
from wind import models


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
