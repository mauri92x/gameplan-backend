# apps/users/urls.py

from django.urls import path
from apps.users.views.auth_views import CustomTokenObtainPairView, RefreshTokenView, MeView, LogoutView

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', RefreshTokenView.as_view(), name='token_refresh'),
    path('me/', MeView.as_view(), name='me'),
    path('logout/', LogoutView.as_view(), name='logout'),
]