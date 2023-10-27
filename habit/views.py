from celery import shared_task
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from habit.models import Habit
from habit.paginators import HabitPaginator
from habit.permissions import IsOwner
from habit.serializers import HabitSerializer, HabitCreateSerializer
from habit.tasks import habits_notification


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        new_habit = serializer.save()
        habits_notification.delay(pk=new_habit.id)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Habit.objects.filter(is_published=True)