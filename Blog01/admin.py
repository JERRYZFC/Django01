# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Blog01.models import MyModel


# Register your models here.
class MyModelAdmin( admin.ModelAdmin ):
	pass

admin.site.register( MyModel, MyModelAdmin )
