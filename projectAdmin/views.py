from django.shortcuts import render, redirect
from project.models import Project, ProjectCategory
from project.forms import ProjectForm

def admin_list_project(request):
    if request.method =='GET':
        projects = Project.objects.all()
        context = {
            'projects': projects,
            'categories':ProjectCategory.objects.all()
        }
        return render(request, 'projectAdmin/projectAdmin.html', context)
    else:
            projects = Project.objects.filter(category__id=request.POST.get('project-category'))
            context  = {
                'filtered_projects': projects,
                'categories':ProjectCategory.objects.all(),
                'projectcat':ProjectCategory.objects.get(id=request.POST.get('project-category'))
            }
            return render(request, 'projectAdmin/projectAdmin.html', context)


        
def admin_search_project(request):
    if request.method == 'POST':
        results = Project.objects.filter(title__icontains=request.POST.get('search'))
        context ={
            'results':results,
            'search':request.POST.get('search')
        }

        return render(request,'projectAdmin/projectAdmin.html', context)
    return redirect('admin_list_project')

def admin_add_project(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ProjectForm()
        else:
            addProject = Project.objects.get(pk=id)
            form = ProjectForm(instance=addProject)
        return render(request,'projectAdmin/add_project_admin.html', {'form':form})
    else:
        if id == 0:
            form = ProjectForm(request.POST, request.FILES)
        else:
            addProject = Project.objects.get(pk=id)
            form = ProjectForm(request.POST,request.FILES, instance = addProject)
        if form.is_valid():
            form.save()
        return redirect('admin_list_project')
# def admin_add_project(request):
#     if request.method == "GET":
#         form = ProjectForm()
#         return render(request,'projectAdmin/add_project_admin.html', {'form':form})
#     else:
#         form = ProjectForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#         return redirect('admin_list_project')

def admin_detail_project(request, id):
    if request.method =='GET':
        project = Project.objects.get(id=id)
        context = {
            'project': project,
        }
        return render(request,'projectAdmin/detail_project.html', context)


def admin_delete_project(request, id):
    project = Project.objects.get(pk=id)
    project.delete()
    return redirect('admin_list_project')