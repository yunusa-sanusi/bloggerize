from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from posts.views import HomePageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('posts/', include('posts.urls', namespace='posts')),
    path('accounts/', include('allauth.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATICFILES_DIRS)
