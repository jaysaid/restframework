# from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework
from rest_framework import filters
from .serializers import *
from .paginations import *
from .filters import *
from django.db import connection
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    用户操作视图
    """
    queryset = User.objects.using('db1').all()
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter,)
    filter_class = UserFilter
    search_fields = ('username',)
    ordering = ('id',)
    
