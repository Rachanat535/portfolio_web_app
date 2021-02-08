from django.shortcuts import render, redirect
from . models import Blog, BlogCategory
from . forms import BlogForm
def list_blog(request):
    if request.method =='GET': 
        blogs = Blog.objects.all()
        new_blogs =Blog.objects.all().order_by('-created_at')
        context = {
            'blogs': blogs,
            'new_blogs':new_blogs,
            'categories':BlogCategory.objects.all()

        }
        return render(request, 'blog/list.html', context)
    else:
        blogs = Blog.objects.filter(category__id=request.POST.get('blog-category'))
        context  = {
            'filtered_blogs': blogs,
            'categories':BlogCategory.objects.all(),
            'blogcat':BlogCategory.objects.get(id=request.POST.get('blog-category'))
        }
        return render(request, 'blog/list.html', context)


def search_blog(request):
    if request.method == 'POST':
        results = Blog.objects.filter(title__icontains=request.POST.get('search'))
        context ={
        'results':results,
        'search':request.POST.get('search')
        }

        return render(request,"blog/list.html", context)
    return redirect('list_blog')

def add_blog(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BlogForm()
        else:
            addBlog = Blog.objects.get(pk=id)
            form = BlogForm(instance=addBlog)
        return render(request,"blog/add_blog.html", {'form':form})
    else:
        if id == 0:
            form = BlogForm(request.POST, request.FILES)
        else:
            addBlog = Blog.objects.get(pk=id)
            form = BlogForm(request.POST,request.FILES, instance = addBlog)
        if form.is_valid():
            form.save()
        return redirect('list_blog')