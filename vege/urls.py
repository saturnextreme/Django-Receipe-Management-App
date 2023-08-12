from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('receipe/', receipes, name='receipes'),
    path('delete/receipe/<id>/', delete_receipes, name='delete_receipe'),
    path('update/receipe/<id>/', update_receipes, name='update_receipe')
]