from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def mypage(request):
    return render(request, 'mypage.html')

def setting(request):
    return render(request, 'setting.html')
    
def home(request):
    return render(request, 'home.html')

def nsctest(request):
    return render(request, 'nsctest.html')