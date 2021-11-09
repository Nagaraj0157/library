from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.http import HttpResponse

def main_view(request):
    return render(request,'myapp/main.html')
def signupform(request):
    a=admin_signupform()
    if request.method=='POST':
        s=admin_signupform(request.POST)
        if s.is_valid():
            name=s.cleaned_data['name']
            email=s.cleaned_data['Email']
            password=s.cleaned_data['password']
            reenter_password=s.cleaned_data['reenter_password']
            if password==reenter_password:
                n=Admin.objects.create(name=name,email=email,password=password)
                n.save()
            else:
                return HttpResponse('password not matched')
            return HttpResponse('user created')
    return render(request,'myapp/sign.html',{'form':a})


def loginform(request):
    a=admin_loginform()
    if request.method=='POST':
        l=admin_loginform(request.POST)
        if l.is_valid():
            email=l.cleaned_data['Email']
            password=l.cleaned_data['password']
            user=Admin.objects.get(email=email)
            if user.email==email and user.password==password:
                return render(request,'myapp/sub.html')
            else:
                return HttpResponse('Plz Enter crrect password')
    return render(request,'myapp/login.html',{'form':a})

def addbook(request):
    a=Book_detailform()
    if request.method=='POST':
        s=Book_detailform(request.POST)
        if s.is_valid():
            Book_Name=s.cleaned_data['Book_Name']
            isbn=s.cleaned_data['isbn']
            Author=s.cleaned_data['Author']
            Language=s.cleaned_data['Language']
            user=Book.objects.create(Book_Name=Book_Name,isbn=isbn,Author=Author,Language=Language)
            user.save()
            return HttpResponse('BOOK ADDED SUCCESSFULLY')
        else:
            return HttpResponse('fill currectly')
    return render(request,'myapp/addbook.html',{'form':a})

def all(request):
     s=Book.objects.all()
     return render(request,'myapp/available.html',{'form':s})
def delete(request,id):
    n=Book.objects.get(id=id)
    n.delete()
    return HttpResponse('record deleted')
def update(request,id):
    n=Book.objects.get(pk=id)
    f=updateform(instance=n)
    if request.method=='POST':
        s=updateform(request.POST,instance=n)
        if s.is_valid():
            s.save()
            return redirect('/showall')
    return render(request,'myapp/update.html',{'form':f})

