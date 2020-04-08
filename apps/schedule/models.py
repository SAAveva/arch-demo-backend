from django.db import models
from django.db.models import Manager

from apps.volunteer.models import Volunteer
from apps.schedule.managers import ScheduleManager

class Schedule(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.CASCADE)

    objects = ScheduleManager()

    def get_free_days(self):
        return FreeDay.objects.filter(schedule=self)

class FreeTime(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    week_day = models.IntegerField()
    time_of_day = models.IntegerField()




