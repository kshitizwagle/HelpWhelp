from django.db import models
from django.utils.timezone import now
import uuid
import os


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('media/', filename)


class Whelp(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to=get_file_path)
    user = models.CharField(max_length=64)
    posted_on = models.DateTimeField(default=now)


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64, error_messages={'required': "Please enter username"}, unique=True)
    email = models.EmailField(max_length=255, error_messages={'required': "Please enter email"})
    phone = models.CharField(max_length=20, error_messages={'required': "Please enter phone number"})
    password = models.CharField(max_length=255, error_messages={'required': "Please enter password"})


class Adopter(models.Model):
    adopter_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    phone = models.CharField(max_length=20, error_messages={'required': "Please enter phone number"})
    email = models.EmailField(max_length=255)

