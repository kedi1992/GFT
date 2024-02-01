from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api.views import CustomerCreateView, LogoutView

urlpatterns = [
    path('token/', obtain_auth_token, name='token_obtain_pair'),
    path('register/', CustomerCreateView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='api-logout'),
]