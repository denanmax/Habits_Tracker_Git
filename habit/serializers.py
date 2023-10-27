from rest_framework import serializers

from habit.models import Habit
from habit.validators import PleasantValidator, LeadTimeValidator, IsPleasantValidator


class PleasureHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('user', 'place', 'time', 'action', 'periodicity', 'is_published', 'lead_time', 'related_habit')


class HabitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ('id', 'user', 'place', 'time', 'action', 'periodicity', 'is_published', 'lead_time', 'related_habit',
                  'is_pleasant_habit', 'reward',)
        validators = [
            LeadTimeValidator(field='lead_time'),
            PleasantValidator(fields),
            IsPleasantValidator(fields='related_habit')
        ]


class HabitSerializer(serializers.ModelSerializer):
    related_habit = PleasureHabitSerializer(many=True)

    class Meta:
        model = Habit
        fields = '__all__'

    def validate(self, data):
        # Валидация полей с помощью валидаторов
        validators = [
            LeadTimeValidator(field='lead_time'),
            PleasantValidator(self.fields),
            IsPleasantValidator(fields='related_habit')
        ]
        for validator in validators:
            validator(data)
        return data
