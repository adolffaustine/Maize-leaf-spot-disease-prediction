from django.shortcuts import render,HttpResponse
from .serializers import MaizeSerializer
from .models import Maize
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class MaizeView(viewsets.ModelViewSet):
    queryset = Maize.objects.all()
    serializer_class = MaizeSerializer

# # Create your views here.
# @api_view(['GET', 'POST'])
# def index(request):
#    if request.method == 'GET':
#       maize_spot = Maize.objects.all()
#       serializer = MaizeSerializer(maize_spot, many= True)
#       return Response(serializer.data)
   
 
#    elif request.method == 'POST':
#       serializer = MaizeSerializer(data=request.data)
#       if serializer.is_valid():
#          serializer.save()
#          return Response(serializer.data, status=status.HTTP_201_CREATED)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
# @api_view(['GET','POST','PUT','DELETE'])
# def maize_details(request,pk):
#       try:
#          maize_spot = Maize.objects.get(pk=pk)

#       except Maize.DoesNotExist:
#          return Response(status=status.HTTP_404_NOT_FOUND)
      
#       if request.method == 'GET':
#          serializer = MaizeSerializer(maize_spot)
#          return Response(serializer.data)
      
#       elif request.method == 'PUT':
        
#          serializer = MaizeSerializer(maize_spot,data=request.data)
#          if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
#       elif request.method == 'DELETE':
#          maize_spot.delete()
#          return Response(status=status.HTTP_204_NO_CONTENT)
    
   