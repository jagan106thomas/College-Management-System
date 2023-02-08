from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_control, never_cache

from StudentApp.models import City, Course, Student_Data

def read_data(request):
    return render(request,'Registration.html',{'data':''})
def regdata_fun(request):
    user_name=request.POST['txtUserName']
    user_email=request.POST['txtUserEmail']
    user_pswd=request.POST['txtUserPswd']
    if User.objects.filter(Q(username=user_name)|Q(email=user_email)).exists():
        return render(request,'Registration.html',{'data':'Username and Email is already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name,email=user_email,password=user_pswd)
        u1.save()
        return redirect('log')
def log_fun(request):
    return render(request,'login.html',{'data':''})
def logdata_fun(request):
    user_name = request.POST['txtUserName']
    user_pswd = request.POST['txtUserPswd']
    user1 = authenticate(username=user_name,password=user_pswd)
    if user1 is not None:
        if user1.is_superuser:
            login(request,user1)
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'User is not Super User'})
    else:
        return render(request,'login.html',{'data':'Enter Proper User Name and Password'})

@login_required
@cache_control(no_cache=True,revalidate=True, nostore=True)
@never_cache
def home_fun(request):
    return render(request,'home.html')

def addstudent_fun(request):
    city=City.objects.all()
    course=Course.objects.all()
    return render(request,'AddStudent.html',{'City_Data':city,'Course_Data':course})

def read_Stud_data(request):
    s1 = Student_Data()
    s1.Stud_Name = request.POST['txtName']
    s1.Stud_Age = request.POST['txtAge']
    s1.Stud_Phno = request.POST['txtPhone']
    s1.Stud_City = City.objects.get(City_Name=request.POST['ddlCity'])
    s1.Stud_Course=Course.objects.get(Course_Name=request.POST['ddlCourse'])
    s1.save()
    return redirect('add')

def display_fun(request):
    s1 = Student_Data.objects.all()
    return render(request, 'display.html', {'data': s1})


def update_fun(request,id):
    s1 = Student_Data.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()
    if request.method == 'POST':
        s1.Stud_Name = request.POST['txtName']
        s1.Stud_Age = request.POST['txtAge']
        s1.Stud_Phno = request.POST['txtPhone']
        s1.Stud_City = City.objects.get(City_Name=request.POST['ddlCity'])
        s1.Stud_Course = Course.objects.get(Course_Name=request.POST['ddlCourse'])
        s1.save()
        return redirect('display')
    return render(request,'update.html',{'data':s1,'City_Data':city,'Course_Data':course})


def delete_fun(request,id):
    s1 = Student_Data.objects.get(id=id)
    s1.delete()
    return redirect('display')

def log_out_fun(request):
    logout(request)
    return redirect('log')