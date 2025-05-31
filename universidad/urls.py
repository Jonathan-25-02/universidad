"""
URL configuration for universidad project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include 
<<<<<<< HEAD
from django.conf import settings
from django.conf.urls.static import static
=======
>>>>>>> c2e7166c1fb100d877013c799ff821e7abfc8f5a

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', include ('Aplicacion.Gestion.urls'))
]
<<<<<<< HEAD

if settings.DEBUG: urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
>>>>>>> c2e7166c1fb100d877013c799ff821e7abfc8f5a
