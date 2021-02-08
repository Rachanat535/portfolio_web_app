from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_list_project, name='admin_list_project'),
    path('search/', views.admin_search_project, name='admin_search_project'),
    path('addproject/', views.admin_add_project, name='admin_add_project'),
    path('projectdetail/<int:id>/',views.admin_detail_project, name = 'admin_detail_project'),
    path('<int:id>', views.admin_add_project, name='admin_update_project'),
    path('delete/<int:id>/', views.admin_delete_project, name = 'admin_delete_project'),


   
]
