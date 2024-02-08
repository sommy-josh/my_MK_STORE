from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from .permissions import CustomPermission
from .serializers import ProductSerializer,UserSerializer
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator



class ProductView(generics.ListCreateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[CustomPermission]
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class UpdateDeleteProduct(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes=[TokenAuthentication]
    permissions_classes=[CustomPermission]

    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer



class PasswordResetConfirmView(generics.ListCreateAPIView):
    def get(self, request, uidb64, token):
        try:
            # Decode uidb64 to get user ID
            user_id = force_str(urlsafe_base64_decode(uidb64))

            # Retrieve user based on user ID
            user = User.objects.get(pk=user_id)

            # Check if the token is valid
            if PasswordResetTokenGenerator().check_token(user, token):
                # Token is valid, you can implement your password reset logic here
                # For example, you might return a success message
                return Response({'detail': 'Password reset successful'}, status=status.HTTP_200_OK)
            else:
                # Token is invalid
                return Response({'detail': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            # Handle exceptions such as invalid uidb64 or user not found
            return Response({'detail': 'Invalid user or token'}, status=status.HTTP_400_BAD_REQUEST)