from django.shortcuts import render, redirect
from .forms import PostCreateForm
from .models import Post
from django.db import  IntegrityError
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def post_list(request):
    context = {
        'post_list' : Post.objects.all(),
    }
    return render(request, 'post/post_list.html',context)

def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post:post_list')
    else:
        form = PostCreateForm()
    return render(request, 'post/post_create.html', {'form':form})


def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username, '', password)
            return render(request, 'login.html', {})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザはすでに登録されています'})


    return render(request, 'signup.html', {})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_profile')

        else:
            return render(request, 'login.html', {})

    return render(request, 'login.html', {})

@login_required
def index_func(request):
    return render(request, 'index.html', {})

def logoutfunc(request):
    logout(request)
    return redirect('login')
