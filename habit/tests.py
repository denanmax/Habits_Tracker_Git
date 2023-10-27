import datetime

from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.models import User
from django.urls import reverse


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.com')
        self.user.set_password('1234')
        self.user.save()

        self.moderator = User.objects.create(email='moderator@moderator.com', is_staff=True)
        self.moderator.set_password('1234')
        self.moderator.save()

        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place='Дома',
            time="2023-10-27T10:58:41.893631Z",
            action='Попить сок',
            is_pleasant_habit=True,
            periodicity=1,
            lead_time="00:00:40",
            is_published=True
        )
        self.habit.save()

    def test_create_habit(self):
        """Тест для создания привычек"""
        url = reverse('habit:habit-create')
        data = {
            'place': 'Дома',
            'time': "2023-10-27T10:58:41.893631Z",
            'action': 'Поскакать на скакалке',
            'is_pleasant_habit': False,
            'periodicity': 2,
            'lead_time': "00:01:40",
            'user': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

        data_error = data
        data_error['lead_time'] = "00:02:40"
        response = self.client.post(url, data_error, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_habits(self):
        """Получение списка привычек"""
        url = reverse('habit:habit-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.force_authenticate(user=self.moderator)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_list_habits_public(self):
        """Список публичных привычек"""
        url = reverse('habit:habit-public')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_retrieve_habit(self):
        """Информации о привычке"""
        url = reverse('habit:habit-view', kwargs={'pk': self.habit.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'], 'Дома')

    def test_update_habit(self):
        """Обновлениe привычки"""
        url = reverse('habit:habit-update', kwargs={'pk': self.habit.id})
        data = {'place': 'Офис'}
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['place'], 'Офис')

    def test_delete_habit(self):
        """Удаление привычки"""
        url = reverse('habit:habit-delete', kwargs={'pk': self.habit.id})
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)