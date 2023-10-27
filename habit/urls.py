from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitDestroyAPIView, \
    HabitUpdateAPIView, PublicHabitListAPIView

app_name = HabitConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit-create'),
    path('habit/', HabitListAPIView.as_view(), name='habit-list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit-view'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit-update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit-delete'),
    path('habit/public/', PublicHabitListAPIView.as_view(), name='habit-public'),
]