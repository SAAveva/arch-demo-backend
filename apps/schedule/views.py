from django.shortcuts import render

from apps.schedule.forms import ScheduleAddForm
from apps.restapi.restapi import api_view

@api_view(methods=['GET'])
def schedule_add(request):
    return ['THIS', 'OBJECT', 'IS', 'SERIALIZED']

@api_view(methods=['GET'])
def schedule_add_form(request):
    form = ScheduleAddForm()
    return form.as_json()
