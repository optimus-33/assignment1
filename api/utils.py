from rest_framework.response import Response
from .models import Accounts
from .serializers import AccountSerializer


def getAccList(request):
    accounts = Accounts.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)