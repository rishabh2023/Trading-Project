from django.urls import path
from .views import *

urlpatterns = [
   path('api/info/', Tradinginfo.as_view(), name='Get Info'),
]
