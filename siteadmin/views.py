from django.shortcuts import render, redirect
from django.http import HttpResponse
from contact.models import Contact
from home.models import Banner
from home.forms import BannerForm
from about.models import Timeline, Expertise, AboutMe
from about.forms import ExpertForm, TimelineForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect


@login_required
def dashbaord(request):
    return render(request, 'siteadmin/index.html')

@login_required
def contact(request):
    context = {'contacts':Contact.objects.all()}

    return render(request, 'siteadmin/contact_admin.html', context)

@login_required
def admin_list_home(request):
    if request.method =='GET': 
        banners = Banner.objects.all()
        context = {
            'banners': banners,

        }
    return render(request, 'siteadmin/home_admin.html', context)

@login_required
def admin_update_home(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = BannerForm()
        else:
            addBanner = Banner.objects.get(pk=id)
            form = BannerForm(instance=addBanner)
        return render(request,'siteadmin/add_banner_admin.html', {'form':form})
    else:
        if id == 0:
            form = BannerForm(request.POST, request.FILES)
        else:
            addBanner = Banner.objects.get(pk=id)
            form = BannerForm(request.POST,request.FILES, instance = addBanner)
        if form.is_valid():
            form.save()
        return redirect('admin_list_home')

@login_required
def admin_about_me(request):
    about = AboutMe.objects.all()
    timelines = Timeline.objects.all()
    expertise =Expertise.objects.all().order_by('-created_at')
    tls = []
    for i in range(len(timelines)):
        rem = i%2
        tls.append([rem, timelines[i]])

    
    context = {
            'timelines': tls,
            'experties': expertise,
            'about' : about
    }
    return render(request, 'siteadmin/AdminAbout/AdminAbout.html', context)


@login_required
def admin_detail_expert(request, id):
    if request.method =='GET':
        experties = Expertise.objects.get(id=id)
        context = {
            'experties': experties,
        }
        return render(request,'siteadmin/Adminabout/detailExpert.html', context)

@login_required       
def admin_update_expert(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = ExpertForm()
        else:
            addExpert = Expertise.objects.get(pk=id)
            form = ExpertForm(instance=addExpert)
        return render(request,'siteadmin/Adminabout/add_expert_admin.html', {'form':form})
    else:
        if id == 0:
            form = ExpertForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                print("added")
                return redirect("admin_about_me")
            else:
                print("INvalid input")
                return redirect("admin_about_me")
        else:
            addExpert = Expertise.objects.get(pk=id)
            form = ExpertForm(request.POST,request.FILES, instance = addExpert)
            if form.is_valid():
                form.save()
            else:
                addExpert.name = request.POST.get("name")
                addExpert.save()
        return redirect('admin_about_me')


@login_required
def admin_update_experience(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TimelineForm()
        else:
            addExperience = Timeline.objects.get(pk=id)
            form = TimelineForm(instance=addExperience)
        return render(request,"siteadmin/adminabout/add_experience_admin.html", {'form':form})
    else:
        if id == 0:
            form = TimelineForm(request.POST, request.FILES)
        else:
            addExperience = Timeline.objects.get(pk=id)
            form = TimelineForm(request.POST,request.FILES, instance = addExperience)
        if form.is_valid():
            form.save()
        return redirect('admin_about_me')

def admin_delete_expert(request, id):
    expert = Expertise.objects.get(pk=id)
    expert.delete()
    return redirect('admin_about_me')

@login_required
def showthis(request):
    
    users= User.objects.all()
    
    context= {'users': users}
        
    return render(request, 'siteadmin/Users/users.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'siteadmin/Users/change_password.html', {
        'form': form
    })