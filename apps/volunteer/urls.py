from django.urls import path, re_path

from apps.volunteer import views

urlpatterns = [
    path('add', views.volunteer_add),
    path('list', views.volunteer_list),
    path('forms/add-volunteer', views.volunteer_add_form),
]
