from django import forms

from apps.schedule.models import Schedule
from apps.reactforms.forms import ReactForm

class ScheduleAddForm(forms.ModelForm, ReactForm):

    class Meta:
        model = Schedule
        fields = ['volunteer']
