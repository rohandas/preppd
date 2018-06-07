# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    school = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

class BehaviouralQuestion(models.Model):
    question = models.TextField()
    def __str__(self):
        return(str(self.question))
