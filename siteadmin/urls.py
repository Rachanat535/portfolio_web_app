from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashbaord, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.admin_about_me, name='admin_about_me'),
    path('home/',views.admin_list_home, name='admin_list_home'),
    path('home/<int:id>',views.admin_update_home, name='admin_update_home'),
    path('expertdetail/<int:id>/',views.admin_detail_expert, name = 'admin_detail_expert'),
    path('<int:id>', views.admin_update_expert, name='admin_update_expert'),
    path('addExpert/', views.admin_update_expert, name='admin_add_expert'),
    path('addexperties/', views.admin_update_experience, name='admin_add_experience'),
    path('updateexperties/<int:id>', views.admin_update_experience, name='admin_update_experience'),
    path('deleteExpert/<int:id>/', views.admin_delete_expert, name="admin_delete_expert"),
    path('users/', views.showthis ,name='users'),
    path('password/', views.change_password, name='change_password')


]