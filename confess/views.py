from django.shortcuts import render,redirect
from .forms import Register,Confess 
from django.contrib.auth.models import User
from .models import Confess_Model

# Create your views here.
def register(response):
    if response.method=="POST":
        form=Register(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:

        form=Register()
    return render(response,"confess/Register.html",{"form":form})
def home(response):
    return render(response,"confess/home.html")
def create_confess(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=Confess(request.POST)
            if form.is_valid():
                confess=request.POST.get("confession")
                user_name=request.user
                print(user_name)
                Confess_Model.objects.create(user=user_name,confession=confess)
                form=Confess()
        else:
                form=Confess()
        return render(request,"confess/create_confession.html",{"form":form})       
    else:
        return redirect("/login")
def my_confession(request):
    if request.user.is_authenticated:
            items=Confess_Model.objects.filter(user=User.objects.get(username=request.user.username).pk)
            return render(request,"confess/my_confession.html",{"items":items})       
    else:
        return redirect("/login")

def all_confession(request):
    if request.user.is_authenticated:
            items=Confess_Model.objects.all()
            return render(request,"confess/my_confession.html",{"items":items})       
    else:
        return redirect("/login")
    