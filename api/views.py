from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Accounts
from .serializers import AccountSerializer
from .utils import getAccList
# Create your views here.

@api_view(['GET','POST'])
def getData(request):
    if request.method == 'GET':
        return getAccList(request)
    
    if request.method == 'POST':
        data = request.data
        par = Accounts.objects.filter(acc_balance__gt=data['acc_balance'])
        serializer = AccountSerializer(par, many=True)
        return Response(serializer.data)