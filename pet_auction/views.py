from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from .serializers import *


class LotListView(APIView):
    def post(self, request):
        serializer = LotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BetListView(APIView):
    def post(self, request):
        serializer = BetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BetDetailView(APIView):
    def patch(self, request, pk):
        bet = Bet.objects.get(pk=pk)
        serializer = BetPatchSerializer(bet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
