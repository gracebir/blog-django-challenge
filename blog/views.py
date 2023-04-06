from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogPost
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import BlogForm, UserForm
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

#register
def registerPage(request):
    page = 'register'
    form = UserForm()
    if(request.method == 'POST'):
        form = UserForm(request.POST)
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

#home page
def homePage(request):
    blogs = BlogPost.objects.filter(status=1)
    context = {'blogs': blogs}
    return render(request, 'blog/home.html', context)

#blog detail
def blogDetail(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    context = {'blog':blog}
    return render(request, 'blog/detail.html', context)

#add a blog 
@login_required(login_url='login')
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


#delete a blog
@login_required(login_url='login')
def deleteBlog(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    if(request.user != blog.author):
        return HttpResponse('You are allowed here!!')
    if(request.method == 'POST'):
        blog.delete()
        return redirect('home')
    return render(request, 'blog/delete_blog.html', {'obj': blog})


#display draft blog
def draftPage(request):
    blogs = BlogPost.objects.filter(status=0)
    context = {'blogs': blogs}
    return render(request, 'blog/draft.html', context)


#update a blog
@login_required(login_url='login')
def updateBlog(request, slug):
    blog = BlogPost.objects.get(slug=slug)
    form = BlogForm(instance=blog)
    if(request.user != blog.author):
        return HttpResponse('You are allowed here!!')
    if(request.method == 'POST'):
        form = BlogForm(request.POST, instance=blog)
        if(form.is_valid()):
            form.save()
            return redirect('home')
    context = {'form': form}   
    return render(request, 'blog/edit_form.html', context)
