from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Tradinginfo(APIView):
    def get(self, request):
        data = request.data
        return Response(data = data,status = status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        return Response(data = data, status=status.HTTP_200_OK)


