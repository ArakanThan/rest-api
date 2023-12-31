"""from django.shortcuts import render"""
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Retrun a list of APIView features"""
        an_apiview = [
         'Uses Http methods as function (get, post, patch, put, delete)',
         'Is simlar to a traditional Django View',
         'Gives you the most control over your app',
         'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview })
