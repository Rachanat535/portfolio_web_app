from django.shortcuts import render
from .forms import SubscribeForm, BannerForm
from .models import Subscription, Banner
from blog.models import Blog, BlogCategory
from project.models import Project, ProjectCategory

def home_page(request):
    banners = Banner.objects.all()
    popularBlogs = Blog.objects.filter(is_popular = True)
    popularProjects = Project.objects.filter(is_popular = True)
    context = {
        'banners': banners,
        'popularBlogs': popularBlogs,
        'popularProjects': popularProjects
    }
    return render(request, 'index.html', context)

def subscribe_form(request, id=0):
    if request.method == "POST":
        
        form = SubscribeForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = SubscribeForm()
            context = {
                'form':form

            }
            return render(request, 'index.html')
