from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='dc-home')
    , path('query', views.query, name='dc-query')
]