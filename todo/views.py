from django.shortcuts import render,redirect
from .models import Create
from .forms import Createform,Createusers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='loginpage')
def Createuser(request):
    user=Createform
    context={
        "users":user
    }
    if request.method=='POST':
        user=Createform(request.POST)
        if user.is_valid():
            user.save()
            messages.success(request, 'A todo added successfully')
            return redirect('show')
       
    return render(request, 'create.html',context)


@login_required(login_url='loginpage')
def update(request ,pk):
    form=Create.objects.get(id=pk)
    user=Createform(instance=form)
    context={
        "users":user
    }
    if request.method=='POST':
        user=Createform(request.POST,instance=form)
        if user.is_valid():
            user.save()
            messages.success(request, 'Information updated successfully')
            return redirect('show')
    return render(request, 'update.html',context)

@login_required(login_url='loginpage')
def delete(request ,pk):
    data=Create.objects.get(id=pk)
    context={
        "data":data
    }
    if request.method=='POST':
        data.delete()
        return redirect('show')
    return render(request, 'delete.html',context)

@login_required(login_url='loginpage')
def show(request):
    user=Create.objects.all()
    context={
        "users":user
    }
    return render(request, 'show.html',context)


def register(request):
    if request.user.is_authenticated:
        return redirect('show')
    else:
        user=Createusers
        context={
            "users":user
        }
        if request.method=='POST':
            user=Createusers(request.POST)
            if user.is_valid():
                user.save()
                messages.success(request,'User created successfully')
                return redirect('loginpage')
        return render(request,'register.html',context)


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('show')
    else:
        if request.method=='POST':
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully as '+ username)
                return redirect('show')
            else:
                messages.warning(request, 'Wrong credentials')
        return render(request, 'login.html')


def logouturl(request):
    logout(request)
    messages.warning(request, 'You have logged out')
    return redirect('loginpage')
