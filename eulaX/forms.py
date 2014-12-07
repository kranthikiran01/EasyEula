
from django import forms
from django.forms import widgets
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib import admin
from eulaX.models import Document
from ckeditor.widgets import CKEditorWidget

class DocumentForm(forms.ModelForm):
	content = forms.CharField(widget=CKEditorWidget())
	class Meta:
		model = Document
		exclude=('uploader','lastEdited','created','slug',)