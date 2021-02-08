from django.shortcuts import render, redirect
from blog.models import Blog, BlogCategory
from blog.forms import BlogForm
def admin_list_blog(request):
    if request.method =='GET': 
        blogs = Blog.objects.all()
        new_blogs =Blog.objects.all().order_by('-created_at')
        context = {
            'blogs': blogs,
            'categories':BlogCategory.objects.all()

        }
        return render(request, 'blogAdmin/blog_admin.html', context)
    else:
        blogs = Blog.objects.filter(category__id=request.POST.get('blog-category'))
        context  = {
            'filtered_blogs': blogs,
            'categories':BlogCategory.objects.all(),
            'blogcat':BlogCategory.objects.get(id=request.POST.get('blog-category'))
        }
        return render(request, 'blogAdmin/blog_admin.html', context)


def admin_search_blog(request):
    if request.method == 'POST':
        results = Blog.objects.filter(title__icontains=request.POST.get('search'))
        context ={
        'results':results,
        'search':request.POST.get('search')
        }

        return render(request,"blogAdmin/blog_admin.html", context)
    return redirect('admin_list_blog')

def admin_add_blog(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BlogForm()
        else:
            addBlog = Blog.objects.get(pk=id)
            form = BlogForm(instance=addBlog)
        return render(request,"blogAdmin/add_blog_admin.html", {'form':form})
    else:
        if id == 0:
            form = BlogForm(request.POST, request.FILES)
        else:
            addBlog = Blog.objects.get(pk=id)
            form = BlogForm(request.POST,request.FILES, instance = addBlog)
        if form.is_valid():
            form.save()
        return redirect('admin_list_blog')

def admin_detail_blog(request, id):
    if request.method =='GET':
        blog = Blog.objects.get(id=id)
        context = {
            'blog': blog,
        }
        return render(request,'blogAdmin/detail_blog.html', context)

def admin_delete_blog(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    return redirect('admin_list_blog')