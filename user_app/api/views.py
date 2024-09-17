from rest_framework.decorators import api_view
from user_app.api.serializers import RegistrationSerializer, userSerializer, userBorrowedBookSerializer
from rest_framework.response import Response
from user_app import models
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from user_app.models import customUser

@api_view(['POST',])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = "Registration successful!"
            data['username'] = account.username
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['email'] = account.email 
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
            
        return Response(data, status=status.HTTP_201_CREATED)
    
class userListView(generics.ListAPIView):
    queryset = models.customUser.objects.all()
    serializer_class = userSerializer
    permission_classes = [IsAdminUser]
    
class AllUsersBorrowedBooksView(generics.ListAPIView):
    permission_classes = [IsAdminUser]  # Restrict access to admin users

    def get(self, request):
        # Fetch all users and their borrowed books
        users = customUser.objects.prefetch_related('borrowed_books').all()
        
        if not users.exists():
            return Response({'message': 'No users found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = userBorrowedBookSerializer(users, many=True)
        
        # Check if any user has borrowed a book
        borrowed_books_exist = any(user['borrowed_books'] for user in serializer.data)
        if not borrowed_books_exist:
            return Response({'message': 'No users have borrowed any books'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    