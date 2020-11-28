# coding=utf-8
# Written By: Nidhi Sahu

from django.urls import include, path
from members.views import TeamMembers
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',  csrf_exempt(TeamMembers.fetch_all), name='fetch_all'),
    path('<int:member_id>/', csrf_exempt(TeamMembers.fetch_id), name='fetch'),
    path('create', csrf_exempt(TeamMembers.create), name='create'),
    path('update/<int:member_id>', csrf_exempt(TeamMembers.update), name='update'),
    path('delete/<int:member_id>', csrf_exempt(TeamMembers.delete), name="delete")
]

