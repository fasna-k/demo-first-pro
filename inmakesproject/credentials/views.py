from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
        n1=request.POST['username']
        n2=request.POST['password']
        user=auth.authenticate(username=n1,password=n2)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid username or password")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        l1=request.POST['username']
        l2= request.POST['first_name']
        l3 = request.POST['last_name']
        l4 = request.POST['email']
        l5 = request.POST['password']
        l6 = request.POST['conf_password']

        if l5==l6:
            if User.objects.filter(username=l1).exists():
                messages.info(request,"username already exist")
                return redirect('register')
            elif User.objects.filter(email=l4).exists():
                messages.info(request,"email already exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=l1,first_name=l2,last_name=l3,password=l5,email=l4)
                user.save()
                print("user created")
                return redirect('login')
        else:
            messages.info(request,"password not matched")
            return redirect('register')

        # return redirect('/')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')