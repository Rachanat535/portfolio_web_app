from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

def contact_me(request):
    context = {'contacts':Contact.objects.all()}
    if request.method=="POST":
        full_name = request.POST['name']
        email = request.POST['email']
        job_title = request.POST['job_title']
        message = request.POST['message']
        ins = Contact(full_name=full_name, email = email, job_title = job_title, message= message)
        ins.save()
    return render(request, 'contact/contact.html', context)