from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Document(models.Model):
	uploader = models.ForeignKey(User)
	title = models.CharField(max_length=1000)
	content = RichTextField(blank=True)
	slug = models.SlugField()
	lastEdited = models.DateTimeField(auto_now=True)
	created =  models.DateTimeField(auto_now_add=True,blank=True)
	def __unicode__(self):
		return str(self.title)+' by '+str(self.uploader)
	@permalink
	def get_absolute_url(self):
		return ('view_document', None, { 'slug': self.slug })