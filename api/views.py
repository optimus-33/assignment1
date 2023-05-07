from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import getAccList, getBalance, getSingle
from .models import APIKey
# Create your views here.

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/api/data/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of Account'
        },
        {
            'Endpoint': '/api/data/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single account info'
        },
        {
            'Endpoint': '/api/data/',
            'method': 'POST',
            'body': {'acc_balance': "<Amount>"},
            'description': 'Fetches account balance greater than the mentioned details'
        },
    ]
    return Response(routes)

@api_view(['GET','POST'])
def getData(request):
    if request.method == 'GET':
        return getAccList(request)
    
    if request.method == 'POST':
        header_key = request.META.get('HTTP_SIYA')
        key_access = APIKey.objects.get(id=1).key
        jas = header_key == key_access
        if jas:
            return getBalance(request)
        else:
            return Response('Sorry, Bro..!')
    
@api_view(['GET'])
def getAccount(request,pk):
    if request.method == 'GET':
        return getSingle(request,pk)