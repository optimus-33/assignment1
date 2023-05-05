from rest_framework.response import Response
from .models import Accounts
from .serializers import AccountSerializer


def getAccList(request):
    accounts = Accounts.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

def getBalance(request):
    data = request.data
    par = Accounts.objects.filter(acc_balance__gt=data['acc_balance'])
    serializer = AccountSerializer(par, many=True)
    return Response(serializer.data)

def getSingle(request,pk):
    accountId = Accounts.objects.get(id=pk)
    serializer = AccountSerializer(accountId, many=False)
    return Response(serializer.data)