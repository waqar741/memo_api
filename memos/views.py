from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Memo
from .serializers import MemoSerializer, MyTokenObtainPairSerializer

class MemoViewSet(viewsets.ModelViewSet):
    serializer_class = MemoSerializer
    permission_classes = [IsAuthenticated] # Ensures only logged-in users can access notes
    parser_classes = [MultiPartParser, FormParser] # For handling photo uploads

    def get_queryset(self):
        user = self.request.user
        return Memo.objects.filter(owner=user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


@api_view(['POST'])
@permission_classes([AllowAny]) # Changed to AllowAny so new users can register
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')

    if not username or not password:
        return Response({'error': 'Username and password required'}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    User.objects.create_user(username=username, password=password, email=email)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
