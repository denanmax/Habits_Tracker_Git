from rest_framework.serializers import ValidationError


class PleasantValidator:
    """Невозможно Одновременно выбрать связанную привычку и приятную привычку."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_is_pleasant = dict(value).get('is_pleasant_habit')
        tmp_is_related = dict(value).get('related_habit')
        tmp_reward = dict(value).get('reward')

        if tmp_is_pleasant and tmp_reward is not None:
            raise ValidationError('У приятной привычки не должно быть вознаграждения!')

        if tmp_is_pleasant and tmp_is_related is not None:
            raise ValidationError('Возможно выбрать либо связанную привычку, либо приятную!')


class IsPleasantValidator:
    """В связанные привычки могут попадать только привычки с признаком приятной привычки.."""
    def __init__(self, fields):
         self.fields = fields

    def __call__(self, value):
        tmp_pleasant = dict(value).get(self.fields)
        if tmp_pleasant:
            if not tmp_pleasant.is_pleasant_habit:
                raise ValidationError('Возможно выбрать в связанную привычку только с признаком приятной привычки!')


class LeadTimeValidator:
    """Время выполнения не должно быть больше 120 секунд"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        lead_time = dict(value).get(self.field)
        if lead_time is not None:
            seconds = lead_time.hour * 3600 + lead_time.minute * 60 + lead_time.second
            if seconds > 120:
                raise ValidationError('Время выполнения не должно превышать 120 сек!')