from django.core.management import BaseCommand

from users.models import User

"""Команда для наполнения базы SuperUser"""
class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='user@user.com',
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('12345')
        user.save()