from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	organisation = models.CharField(max_length=4000)
	address = models.CharField(max_length=4000)