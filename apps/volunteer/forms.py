from django import forms

from apps.volunteer.models import Volunteer
from apps.reactforms.forms import ReactForm

class VolunteerAddForm(forms.ModelForm, ReactForm):
    class Meta:
        fields = ['first_name', 'last_name', 'email', 'username','password']
        model = Volunteer
