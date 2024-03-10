import firebase_admin
from firebase_admin import auth
from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from .auth_decorator import firebase_auth_required

@api_view(['GET'])
def public_api(request):
    try:
        return Response({"message": "Hello! this is public api."})
    except Exception as e:
        return Response({"error": "Unauthorized access. Please authenticate."}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
@firebase_auth_required
def my_protected_api(request):
    # Access user data from the request
    user_data = request.user_data
    # Your view logic here
    return JsonResponse({"message": "This is a protected API.", "user_data": user_data})
