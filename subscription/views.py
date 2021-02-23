from django.shortcuts import render

from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


from .models import UserSubscription
from .serializer import UserSubscriptionSerialiser


class UserSubscriptionView(generics.ListAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerialiser


    def post(self, request):
        serializer = UserSubscriptionSerialiser(data=request.data)
        if serializer.is_valid():
            try:
                UserSubscription.objects.get(user=serializer.validated_data['user'])
                return Response({'error': 'user already subscribed'}, status=status.HTTP_400_BAD_REQUEST)
            except:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RemoveSubscriptionView(generics.DestroyAPIView):
    queryset = UserSubscription.objects.all()
    serializer_class = UserSubscriptionSerialiser
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


    def get(self, *args, **kwargs):
        try:
            queryset = UserSubscription.objects.get(id=self.kwargs['id'])
            serializer_class = UserSubscriptionSerialiser(queryset)
            return Response(serializer_class.data)
        except:
            return Response({'error':f'No data found with id: {self.kwargs["id"]}'})

