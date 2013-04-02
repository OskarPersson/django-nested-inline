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
