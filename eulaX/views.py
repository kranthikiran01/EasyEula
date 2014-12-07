from django.shortcuts import render,render_to_response,get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from eulaX.models import Document
from eulaX.forms import DocumentForm
from django.template.defaultfilters import slugify
# Create your views here.
def index(request):
	return render(request,'eulaX/dashboard.html',{'title':request.user.userprofile.organisation})

def document(request):
	if request.method == "POST":
		document_form=DocumentForm(data=request.POST)
		if document_form.is_valid():
			document = document_form.save(commit = False)
			document.uploader=request.user
			document.slug = slugify(str(document.title))
			document.save()
			messages.info(request,'You successfully created a document with EasyEula. Thank you.')
			return HttpResponseRedirect('/dashboard/')
		else:
			messages.error(request,str(document_form.errors))
	else:
		document_form=DocumentForm()
	return render(request,'eulaX/document.html',{'document_form':document_form})

def listDocuments(request):
	document=Document()
	document=Document.objects.filter(uploader=request.user).select_related()
	return render(request,'eulaX/listDocuments.html',{'documents':document})

def viewDocument(request,slug):
	return render(request,'eulaX/viewDocument.html',{'document':get_object_or_404(Document,slug=slug)})