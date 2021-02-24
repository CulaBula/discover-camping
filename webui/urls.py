from django.urls import path
from . import views 

urlpatterns = [    
    path('query', views.query, name='dc-query')
    , path('', views.query_submit, name='dc-query_submit')
]