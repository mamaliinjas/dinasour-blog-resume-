from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import CarnivorousPost , pterosaursPost ,herbivoresPost 



# Create your views here.
def index(request):
    return render(request , 'index.html')
def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request , 'username is already taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username , password=password , email=email)
                user.save()
                messages.success(request , 'account created succesfully')
                return redirect ('login')    
        else:
            messages.info(request , 'password not same')
            return redirect('register')  
    else:           
        return render(request , 'register.html')
    
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request , username=username ,password=password )
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request , 'invalid crendital')
            return redirect('login')            
    else:
        return render(request , 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect ('/')

def contact(request):
    return render(request , 'contact.html')

def Carnivorous(request):
    posts=CarnivorousPost.objects.all()
    return render(request , 'Carnivorous.html' , {'posts' : posts})

def herbivores(request):
    posts=herbivoresPost.objects.all()
    return render(request , 'herbivores.html' , {'posts' : posts})

def pterosaurs(request):
    posts=pterosaursPost.objects.all()
    return render(request , 'pterosaurs.html' , {'posts' : posts})