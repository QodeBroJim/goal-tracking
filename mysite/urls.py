from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('accounts/', include('users.urls')),
	path('accounts/', include('django.contrib.auth.urls')),
    path('goals/', include('goals.urls')),
    path('journal/', include('journal.urls')),
    path('affirmations/', include('affirmations.urls')),
    
    # 3rd Party URL's
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('badgify/', include('badgify.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
