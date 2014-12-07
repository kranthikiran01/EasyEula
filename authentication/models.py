from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	phoneNumber = models.CharField(max_length=30)
	organisation = models.CharField(max_length=100)
	signUpDate = models.DateField(auto_now=True)
	picture = models.ImageField(upload_to='profile_pictures',blank=True)
	ipaddress = models.URLField(max_length=25)
	content = RichTextField()
	def __unicode__(self):
		return self.organisation