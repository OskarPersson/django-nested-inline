django-nested-inline
====================

Nested inline support for Django admin

Most of the code from this package is from [https://code.djangoproject.com/ticket/9025](https://code.djangoproject.com/ticket/9025)

Github
------

[https://github.com/s-block/django-nested-inline](https://github.com/s-block/django-nested-inline)


Installation
------------

pip install django-nested-inline


Usage
-----

Add `nested_inline` to `INSTALLED_APPS`

models.py

    from django.db import models

    class TopLevel(models.Model):
        name = models.CharField(max_length=200)

    class LevelOne(models.Model):
        name = models.CharField(max_length=200)
        level = models.ForeignKey('TopLevel')

    class LevelTwo(models.Model):
        name = models.CharField(max_length=200)
        level = models.ForeignKey('LevelOne')

    class LevelThree(models.Model):
        name = models.CharField(max_length=200)
        level = models.ForeignKey('LevelTwo')


admin.py

    from django.contrib import admin
    from nested_inline.admin import NestedStackedInline, NestedModelAdmin
    from example.models import *

    class LevelThreeInline(NestedStackedInline):
        model = LevelThree
        extra = 1
        fk_name = 'level'


    class LevelTwoInline(NestedStackedInline):
        model = LevelTwo
        extra = 1
        fk_name = 'level'
        inlines = [LevelThreeInline]


    class LevelOneInline(NestedStackedInline):
        model = LevelOne
        extra = 1
        fk_name = 'level'
        inlines = [LevelTwoInline]


    class TopLevelAdmin(NestedModelAdmin):
        model = TopLevel
        inlines = [LevelOneInline]


    admin.site.register(TopLevel, TopLevelAdmin)



Changelist
----------

0.4.3 - Added support for Django >= 3.2

0.4.2 - Fix assets

0.4.1 - Fix permission checks

0.4.0 - Added support for Django 3.0

0.3.7 - added support for django 1.10, fix unique fieldset id

0.3.6 - added support for django 1.9

0.3.5 - Removed deprecated methods and updated for Django 1.8/1.9

0.3.4 - added licence and updated for python 3

0.3.3 - fixed bug where inlines without inlines would cause an error
