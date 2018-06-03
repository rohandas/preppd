from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^welcome$', views.view_landing_page),
    url(r'^profile$', views.view_profile_page),
    url(r'^getting-started$', views.view_getting_started_page),
    url(r'^signin$', views.view_signin_page),
    url(r'^signup$', views.view_signup_page),
    url(r'^math$', views.view_mental_math_dashboard_page),
    url(r'^structuring$', views.view_structuring_practice_page),
    url(r'^buddy-finder$', views.view_buddy_finder_page),
    url(r'^nav$', views.nav),
    url(r'^header$', views.header),
    url(r'^math-practice$', views.view_mental_math_practice_page),
    url(r'^getting-started-intro$', views.view_getting_started_intro_page),
    url(r'^getting-started-industry$', views.view_getting_started_industry_page),
    url(r'^getting-started-firms$', views.view_getting_started_firms_page),
    url(r'^getting-started-cases$', views.view_getting_started_cases_page),
    url(r'^getting-started-behaviourals$', views.view_getting_started_behaviourals_page),
    url(r'^qualitative-analysis$', views.view_qualitative_analysis_page),
    url(r'^quantitative-analysis$', views.view_quantitative_analysis_page),
    url(r'^ideation$', views.view_ideation_page),
    url(r'^full-case$', views.view_full_case_page),
    url(r'^story-planning$', views.view_story_planning_page),
    url(r'^behavioural-practice$', views.view_behavioural_practice_page),
    url(r'^interview-me$', views.view_interview_me_page),
    url(r'^test$', views.test),
]
