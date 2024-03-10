from django.http import JsonResponse
from functools import wraps
from firebase_admin import auth

def firebase_auth_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        firebase_token = request.META.get('HTTP_AUTHORIZATION', '').split('Bearer ')[-1]
        if not firebase_token:
            return JsonResponse({"error": "No authentication token provided."}, status=401)
        try:
            decoded_token = auth.verify_id_token(firebase_token)
            uid = decoded_token['uid']
            user = auth.get_user(uid)
            print(user._data)
            user_data = {
                "user_id": user._data['localId'],
                "email": user._data['email']
            }
            request.user_data = user_data
            return view_func(request, *args, **kwargs)
        except auth.InvalidIdTokenError:
            return JsonResponse({"error": "Unauthorized access. Please authenticate."}, status=401)
    return wrapper
