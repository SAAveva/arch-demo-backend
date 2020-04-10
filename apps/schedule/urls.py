from django.urls import path, re_path

from apps.schedule import views

urlpatterns = [
    path('add', views.schedule_add),
    path('forms/add-schedule', views.schedule_add_form),
]
