from django.urls import path
from .views import ListMenu

urlpatterns = [
    path('look/',ListMenu.as_view(),name='get_all_menu'),

]