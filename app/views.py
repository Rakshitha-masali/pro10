from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view1(request):
    return HttpResponse("<h1>Hello world</h1>")

def view2(request,email):
    return render(request,"sample.html",context={'email':email,'name':"rakshitha"})

def view3(request,name):
    return HttpResponse(f'<h1>Hello{name}</h1>')

def if_demo(request):
    login=True
    return render(request,"if_demo.html",context={'login':login})

def ifelse_demo(request):
    login=True
    return render(request,"ifelse_demo.html",context={'login':login,'name':'rakshitha','a':10,'b':50})

def for_demo(request):
    return render (request,"for_demo.html",context={"item":['apple','ball','cat'],\
        'profile':{'name':"rakshitha","age":22,}})
