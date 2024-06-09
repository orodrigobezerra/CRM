from django.urls import path
from . import views

urlpatterns = [
  path('create-lead', views.create_lead, name='create_lead'),
  path('read_lead', views.read_lead, name='read_lead'),
  path('update_lead', views.update_lead, name='update_lead'),
  path('delete_lead', views.delete_lead, name='delete_lead'),
]