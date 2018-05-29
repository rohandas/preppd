from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile$', views.view_profile_page),
    url(r'^getting-started$', views.view_getting_started_page),
    url(r'^signin$', views.view_signin_page),
    url(r'^signup$', views.view_signup_page),
    url(r'^math$', views.view_mental_math_practice_page),
]
