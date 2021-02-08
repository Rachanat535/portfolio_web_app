from django.urls import path
from . import views


urlpatterns = [
    path('', views.admin_list_blog, name='admin_list_blog'),
    path('search/', views.admin_search_blog, name='admin_search_blog'),
    path('addblog/', views.admin_add_blog, name='admin_add_blog'),
    path('blogdetail/<int:id>/',views.admin_detail_blog, name = 'admin_detail_blog'),
    path('<int:id>', views.admin_add_blog, name='admin_update_blog'),
    path('delete/<int:id>/', views.admin_delete_blog, name = 'admin_delete_blog'),

]