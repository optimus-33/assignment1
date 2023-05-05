from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import getAccList, getBalance, getSingle
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
        return getBalance(request)
    
@api_view(['GET'])
def getAccount(request,pk):
    if request.method == 'GET':
        return getSingle(request,pk)