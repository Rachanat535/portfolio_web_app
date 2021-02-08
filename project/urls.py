from django.urls import path
from . import views


urlpatterns = [
    path('', views.list_project, name='list_project'),
    path('search/', views.search_project, name='search_project'),
    path('addproject/', views.add_project, name='add_project')
   
]
