from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def loginPage(request):
    page = 'login'
    if(request.user.is_authenticated):
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')
        
    context = {'page': page}
    
    return render(request, 'blog/login_register.html', context)

def registerPage(request):
    page = 'register'
    form = UserCreationForm()
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An occurred during registration')
    
    context = {'form': form, 'page': page}
    
    return render(request, 'blog/login_register.html', context)


#logout user
def logoutUser(request):
    logout(request)
    return redirect('home')

def homePage(request):
    blogs = BlogPost.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog/home.html', context)

def blogDetail(request, slug):
    return HttpResponse('blog Detail')

def write(request):
    status = 0
    if(request.method == 'POST'):
        title = request.POST.get('title')
        slug = request.POST.get('slug')
        author = request.user
        content = request.POST.get('content')
        status_str = request.POST.get('status')
        print('content',content)
        if(status_str == 'Publish'):
            status = 1
        else:
            status = 0
        blog = BlogPost(title=title, slug=slug, author=author, content=content, status=int(status))
        blog.save()
    context = {}
    return render(request, 'blog/write_form.html', context)
