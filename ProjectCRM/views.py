from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from crm.models import UserProfileManager

def acc_login(request):
    errors = {}
    if request.method == "POST":
        _email = request.POST.get("email")
        _password = request.POST.get("password")
        user = authenticate(username=_email, password=_password)
        if user:
            login(request, user)
            next_url = request.GET.get("next", "/")
            return redirect(next_url)
        else:
            errors['error'] = "请先创建用户!"
    return render(request, "login.html", {"errors": errors})

def acc_logout(request):
    logout(request)
    return redirect("/account/login/")

def index(request):
    return render(request, 'index.html')

def create(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        u = UserProfileManager()
        u.create_superuser(email, username, password)
        return redirect('account/login/')
    return render(request, 'create.html')
