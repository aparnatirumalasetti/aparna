from django.db import models
from django.contrib.auth.models import User
from .managers import PersonManager

class Person(User):
    objects= PersonMananager()
     class  Meta:
         proxy = True
         ordering = ('first_namr', )
     def do_something(self):
         pass

# Create your models here.
