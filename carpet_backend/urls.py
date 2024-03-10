# from django.urls import path
# from accounts import views

# urlpatterns = [
#     path('hello/', views.HelloView.as_view(), name='hello'),
# ]








from django.urls import path
from accounts.views import my_protected_api, public_api
urlpatterns = [
    path('public_api/', public_api, name='public_api'),
    path('my_protected_api/', my_protected_api, name='my_protected_api'),
]