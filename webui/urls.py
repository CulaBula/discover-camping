from django.urls import path
from . import views 

urlpatterns = [    
    path('', views.query, name='dc-query')
    , path('query_submit', views.query_submit, name='dc-query_submit')
    , path('home', views.home, name='dc-home')
]