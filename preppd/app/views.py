# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view_profile_page(request):
    return render(request, 'dashboard.html', {})

def view_getting_started_page(request):
    return render(request, 'getting-started.html', {})

def view_signin_page(request):
    return render(request, 'signin.html', {})

def view_signup_page(request):
    return render(request, 'signup.html', {})
