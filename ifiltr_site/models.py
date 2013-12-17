from django.db import models

# Create your models here.
class Person(models.Model):
  fname = models.CharField(max_length=50)
  lname = models.CharField(max_length=50)
  gender = models.CharField(max_length=1,
    choices=(('m','male'),('f','female')))

class clickThrough(models.Model):
  person = models.ForeignKey(Person)
  item = models.URLField()

class Category(models.Model):
  parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
  name = models.CharField(max_length=50)
  depth = models.IntegerField()
  

