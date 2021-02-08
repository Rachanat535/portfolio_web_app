from django.shortcuts import render, redirect
from . models import Project, ProjectCategory
from . forms import ProjectForm

def list_project(request):
    if request.method =='GET':
        projects = Project.objects.all()
        new_projects = Project.objects.all().order_by('-created_at')
        context = {
            'projects': projects,
            'new_projects': new_projects,
            'categories':ProjectCategory.objects.all()
        }
        return render(request, 'project/project.html', context)
    else:
            projects = Project.objects.filter(category__id=request.POST.get('project-category'))
            context  = {
                'filtered_projects': projects,
                'categories':ProjectCategory.objects.all(),
                'projectcat':ProjectCategory.objects.get(id=request.POST.get('project-category'))
            }
            return render(request, 'project/project.html', context)


        
def search_project(request):
    if request.method == 'POST':
        results = Project.objects.filter(title__icontains=request.POST.get('search'))
        context ={
            'results':results,
            'search':request.POST.get('search')
        }

        return render(request,"project/project.html", context)
    return redirect('list_project')


def add_project(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProjectForm()
        else:
            addProject = Project.objects.get(pk=id)
            form = ProjectForm(instance=addProject)
        return render(request,"project/add_project.html", {'form':form})
    else:
        if id == 0:
            form = ProjectForm(request.POST, request.FILES)
        else:
            addProject = Project.objects.get(pk=id)
            form = ProjectForm(request.POST,request.FILES, instance = addProject)
        if form.is_valid():
            form.save()
        return redirect('list_project')