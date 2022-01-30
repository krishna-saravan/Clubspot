from django.shortcuts import render
from .models import UserAccount
from rest_framework import status
from .serializers import UserAccount_serializer, UpdateUserAccount_serializer
from rest_framework.decorators import api_view
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class register_view(UpdateAPIView):
    # queryset = UserAccount.objects.all()

    serializer_class = UpdateUserAccount_serializer
    permission_classes = (
        IsAuthenticated,
        )
    lookup_field = "id"

    def get_object(self,queryset=None):
        return UserAccount.objects.filter(email = self.request.user.email).first()






@api_view(['GET'])
def profile_view(request):
    user = request.user

    serializer = UserAccount_serializer(user, many = False)

    return Response(serializer.data)
