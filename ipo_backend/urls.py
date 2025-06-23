"""
URL configuration for ipo_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ipos.urls')),  # include ipos app URLs
]

##By default, Django doesn’t serve uploaded files (like images) in development.
#Serve Media Files in Development
##uploaded images will be served when running the development server.
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

''''| Code                                | What it means                                                              |
| ----------------------------------- | -------------------------------------------------------------------------- |
| `static(settings.MEDIA_URL, ...)`   | Tells Django to create a route like `/media/...`                           |
| `document_root=settings.MEDIA_ROOT` | Connects that route to the folder where files are stored (`media/` folder) |
'''

