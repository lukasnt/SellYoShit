from django.shortcuts import render

from .serializers import *
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions



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
    def get(self, request, pk):
        sale_item = self.get_object(pk)

        if not sale_item:
            return JsonResponse({'status': 0, 'message': 'User with this id not found'})
        serializer = SaleItemSerializer(data = sale_item)

        if serializer.is_valid():
            return JsonResponse(serializer.data, safe=False) 
        else:
            return Response({"response" : "error", "message" : serializer.errors})



    def post(self, request, pk):

        try:
            sale_item = self.get_object(pk)
        except:
            return JsonResponse({'status': 0, 'message': 'User with this id not found'})

        title = request.data.get("title", None)
        description = request.data.get('description', None)
        creator = get_current_user()
        img = null

        sale_item.title = title
        sale_item.description = description
        sale_item.creator = creator
        sale_item.img = img

        try:
            sale_item.save()
            return JsonResponse({'status': 1, 'message': 'Your ad created successfully!'})
        except:
            return JsonResponse({'status': 0, 'message': 'There was something wrong while creating your ad.'})
