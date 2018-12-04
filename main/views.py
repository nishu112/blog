
from django.contrib import auth

from .models import *
from .forms import *
from django.shortcuts import HttpResponse,render,redirect
from .import views
import json

def index(request):
	AllData=Entry.objects.all()
	if request.method=='POST':
		details=EntryForm(request.POST)
		print('got here')
		if details.is_valid():
			temp=details.save(commit=False)
			temp.save()
			return redirect('index')
		else:
			return render(request,"structure.html",{'form':details,'AllData':AllData})
	else:
		form=EntryForm(None)
		return render(request,"structure.html",{'form':form,'AllData':AllData})
