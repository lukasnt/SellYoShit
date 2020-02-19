from django.shortcuts import render

from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import SaleItemSerializer
from .models import SaleItem
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


@api_view(['GET'])
def get_current_user(request):
    serializer = GetFullUserSerializer(request.user)
    return Response(serializer.data)


class CreateUserView(APIView):
    permission_classes = (permissions.AllowAny, )
    def post(self,request):
        user = request.data.get('user')
        if not user:
            return Response({'response' : 'error', 'message' : 'No data found'})
        serializer = UserSerializerWithToken(data = user)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            return Response({"response" : "error", "message" : serializer.errors})
        return Response({"response" : "success", "message" : "user created succesfully"})

class SaleItemView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        saleItems = SaleItem.objects.all()
        serializer = SaleItemSerializer(saleItems, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        si_serializer = SaleItemSerializer(data=request.data)
        if si_serializer.is_valid():
            si_serializer.save()
            return Response(si_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', si_serializer.errors)
            return Response(si_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
