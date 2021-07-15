from django.urls import path

urlpatterns = [
   path('api/info/', Tradinginfo.as_view(), name='Get Info'),
]
