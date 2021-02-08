from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('admin/', include('siteadmin.urls')),
    path('admin/project/', include('projectAdmin.urls')),
    path('admin/blog/', include('blogAdmin.urls')),
    path('auth/', include('authentication.urls')),
    path('blog/', include('blog.urls') ),
    path('project/', include('project.urls') ),
    path('about-me/', include('about.urls') ),
    path('contact_me/', include('contact.urls') ),
    path('', include('home.urls'))
]  + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
 