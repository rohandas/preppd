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

def view_mental_math_dashboard_page(request):
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

def header(request):
    return render(request, 'header.html', {})

def view_mental_math_practice_page(request):
    return render(request, 'math-practice.html', {})

def view_getting_started_intro_page(request):
    return render(request, 'getting-started/getting-started-intro.html', {})

def view_getting_started_industry_page(request):
    return render(request, 'getting-started/getting-started-industry.html', {})

def view_getting_started_firms_page(request):
    return render(request, 'getting-started/getting-started-firms.html', {})

def view_getting_started_cases_page(request):
    return render(request, 'getting-started/getting-started-cases.html', {})

def view_getting_started_behaviourals_page(request):
    return render(request, 'getting-started/getting-started-behaviourals.html', {})

def view_qualitative_analysis_page(request):
    return render(request, 'cases/qualitative-analysis.html', {})

def view_quantitative_analysis_page(request):
    return render(request, 'cases/quantitative-analysis.html', {})

def view_ideation_page(request):
    return render(request, 'cases/ideation.html', {})

def view_full_case_page(request):
    return render(request, 'cases/full-case.html', {})

def view_story_planning_page(request):
    return render(request, 'behaviourals/story-planning.html', {})

def view_behavioural_practice_page(request):
    return render(request, 'behaviourals/behavioural-practice.html', {})

def view_interview_me_page(request):
    return render(request, 'interview-me.html', {})

def view_expert_call_page(request):
    return render(request, 'expert-call.html', {})

def view_expert_review_page(request):
    return render(request, 'expert-review.html', {})

def test(request):
    return render(request, 'test.html', {})
