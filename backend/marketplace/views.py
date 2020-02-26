from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView)
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import SaleItemSerializer
from .models import SaleItem
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .permissions import IsOwnerProfileOrReadOnly
from .models import User
# from .serializers import UserSerializer
from djoser.serializers import UserSerializer


class UserProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class SaleItemView(ModelViewSet):
    permission_classes = (permissions.AllowAny, )
    serializer_class = SaleItemSerializer
    queryset = SaleItem.objects.all()
