
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Tradinginfo(APIView):
    def get(self, request):
        data = request.data
        print(data)
        return Response(data = data,status = status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        print(data)
        return Response(data = data, status=status.HTTP_200_OK)


