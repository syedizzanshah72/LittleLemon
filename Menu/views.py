from django.shortcuts import render
from .serializers import MenuSerializer
from .models import Menu
from rest_framework import mixins,response
from rest_framework.generics import GenericAPIView

class ListMenu(mixins.ListModelMixin,GenericAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    
