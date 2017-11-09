"""CholitoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from CholitoProject import settings
from CholitoProject.views import AuthView, LogOutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^complaint/', include('complaint.urls')),
    url(r'^auth/', AuthView.as_view(), name='auth'),
    url(r'^logout/', LogOutView.as_view(), name='logout'),
    url(r'^municipality/', include('municipality.urls')),
    url(r'^animal/', include('animals.urls')),
    url(r'', include('naturalUser.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
