from django.contrib import admin

# Register your models here.
from .models import Project, ProjectCategory

admin.site.register(Project)
admin.site.register(ProjectCategory)
