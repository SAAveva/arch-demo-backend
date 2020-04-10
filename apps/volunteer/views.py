from django.shortcuts import render
from django.template.context_processors import csrf

from apps.restapi.restapi import api_view, Http500

from apps.volunteer.forms import VolunteerAddForm
from apps.volunteer.models import Volunteer

@api_view(methods=['POST'])
def volunteer_add(request):
    form = VolunteerAddForm(request.POST)
    if form.is_valid():
        form.save()
        return {'status': 'success'}
    else:
        raise Http500(form.errors.as_json())

@api_view(methods=['GET'])
def volunteer_list(request):
    return [{'name': v.first_name, 'email': v.email}
                for v in Volunteer.objects.all()]
    
@api_view(methods=['GET'])
def volunteer_add_form(request):
    form = VolunteerAddForm()
    return form.as_json('POST')
    
