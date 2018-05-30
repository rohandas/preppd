# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

import random

# Create your views here.

def view_landing_page(request):
    return render(request, 'landing.html', {})

def view_profile_page(request):
    return render(request, 'dashboard.html', {})

def view_getting_started_page(request):
    return render(request, 'getting-started.html', {})

def view_signin_page(request):
    return render(request, 'signin.html', {})

def view_signup_page(request):
    return render(request, 'signup.html', {})

def view_mental_math_practice_page(request):
    num1 = random.randint(1, 1000)
    num2 = random.randint(2,40)
    operator = random.randint(1,4)
    if operator == 1:
        operator = '+'
        answer = num1+num2
    elif operator == 2:
        operator = '-'
        answer = num1-num2
    elif operator == 3:
        operator = '*'
        answer = num1*num2
    else:
        operator = '/'
        answer = num1/num2

    context = {'num1':num1, 'num2':num2, 'operator':operator, 'answer':answer}
    return render_to_response('math.html', context)

def view_structuring_practice_page(request):
    return render(request, 'structuring.html', {})

def view_getting_started_page(request):
    return render(request, 'getting-started.html', {})

def view_buddy_finder_page(request):
    return render(request, 'buddy-finder.html', {})

def nav(request):
    return render(request, 'nav.html', {})

def test(request):
    return render(request, 'test.html', {})
