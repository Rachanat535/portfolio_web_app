from django.shortcuts import render
from . models import Timeline, Expertise, AboutMe

def about_me(request):
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
    return render(request, 'about/about.html', context)