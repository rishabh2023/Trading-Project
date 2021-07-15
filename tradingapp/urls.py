from django.urls import path
from .views import *

urlpatterns = [
   path('', Tradinginfo.as_view(), name='Get Info'),
]
