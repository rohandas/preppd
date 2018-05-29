# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

import random

# Create your views here.

def view_profile_page(request):
    return render(request, 'dashboard.html', {})

def view_getting_started_page(request):
    return render(request, 'getting-started.html', {})

def view_signin_page(request):
    return render(request, 'signin.html', {})

def view_signup_page(request):
    return render(request, 'signup.html', {})

def view_mental_math_practice_page(request):
    numerator = random.randint(1, 1000)
    denominator = random.randint(2,40)
    context = {'numerator':numerator, 'denominator':denominator}
    return render_to_response('math.html', context)
