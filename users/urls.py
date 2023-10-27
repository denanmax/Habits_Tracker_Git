from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserListAPIView, UserCreateAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', UserListAPIView.as_view(), name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-create'),
    path('update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('view/', UserRetrieveAPIView.as_view(), name='user-view'),
    path('delete/', UserDestroyAPIView.as_view(), name='user-delete'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
