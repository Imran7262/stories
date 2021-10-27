from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import *
from .models import *


# Create your views here.
def home(request):
    cat = category.objects.all()
    photo = photos.objects.all()
    context = {'cat': cat, 'photo': photo}
    return render(request, 'home.html', context)


def catwise(request,cid):
    cat = category.objects.all()
    catt= category.objects.get(id=cid)
    photo=photos.objects.filter(ctg=catt)
    context = {'cat': cat, 'photo': photo}
    return render(request, 'home.html', context)

def contact(request):
    if request.method == 'POST':
        data = cate(request.POST, request.FILES)
        if data.is_valid():
            data.save()

    a = cate()

    context = {'a': a}
    return render(request, 'contact.html', context)





def register(request):
    if request.method == "POST":
        zname = request.POST.get("fname")
        zlname = request.POST.get("lname")
        zuname = request.POST.get("uname")
        zmail = request.POST.get("mail")
        zpas = request.POST.get("pass")
        zpass = request.POST.get("pass2")
        if zpas != zpass:
            messages.warning(request, 'password does not match')
            return redirect(register)

        elif User.objects.filter(username=zuname).exists():
            messages.warning(request, 'username already taken')
            return redirect('register')

        elif User.objects.filter(email=zmail).exists():
            messages.warning(request, 'email already taken')
            return redirect('register')

        else:

            user = User.objects.create_user(first_name=zname, last_name=zlname, username=zuname, email=zmail,
                                            password=zpas)
            user.save()
            return redirect('lagin')

    return render(request, 'register.html')


def lagin(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        pas = request.POST.get("pass")
        user = authenticate(username=uname, password=pas)
        if user is not None:
            login(request, user)
            messages.success(request, 'login succesful')
            return redirect('/')
        else:
            messages.warning(request, 'invalid input please check')
            return redirect('login')

    return render(request, 'login.html')


def lout(request):
    logout(request)
    return redirect('/')


def imageupload(request):
    if request.method == 'POST':
        image = img(request.POST, request.FILES)
        if image.is_valid():
            image.save()
            return redirect('/')
    image = img()
    context = {'image': image}
    return render(request, 'imageupload.html', context)


def aply_for_story(request):
    if request.method=='POST':
        story=for_astory(request.POST ,request.FILES)
        if story.is_valid():
            story.save()
            messages.success(request,"wait for the approval............thankx")
            return redirect('aply_for_story')
    story=for_astory()
    context={'story':story}
    return render(request,'aply_story.html', context)