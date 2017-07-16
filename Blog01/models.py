# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class MyModel( models.Model ):
	model_title = models.CharField( max_length=250, help_text='Maximum 250 characters.' )
	model_content = models.TextField( blank = True )