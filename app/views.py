from django.shortcuts import render

# Create your views here.
def agriculture(request):
    return render(request,'agriculture.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def registation(request):
    return render(request,'registation.html')

def details(request):
    return render(request,'details.html')