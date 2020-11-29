# coding=utf-8
# Written By: Nidhi Sahu
from django import views
from django.shortcuts import render


class Welcome(views.View):

    @staticmethod
    def welcome(request):
        return render(request, "welcome.html")
