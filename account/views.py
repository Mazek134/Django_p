from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import  UserCreationForm
from .forms import LoginForm
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.

from django.contrib.auth.decorators import login_required

def register(request):

 if request.method =='POST':

  form = UserCreationForm(request.POST)
  if form.is_valid():

   form.save()
   return render(request, 'registration/after_register.html')

 else:

  form= UserCreationForm()

 return render(request,'registration/register.html',{'form':form})


def mozenowelog(request):


 return render(request,'registration/mozenowelog.html')



@login_required

def dashboard(request):

 return render(request,'account/dashboard.html', {'section': 'dashboard'})


