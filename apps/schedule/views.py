from django.shortcuts import render

from apps.schedule.forms import ScheduleAddForm
from apps.restapi.resolver import api

# schedule/add
# schedule/edit
# schedule/

@api('/api/schedule/add', methods=['POST'])
def schedule_add(request):
    return ['THIS', 'OBJECT', 'IS', 'SERIALIZED']

@api('/api/schedule/forms', methods=['GET'])
def schedule_add_form(request):
    form = forms.ScheduleForm()
    return form.as_json()
