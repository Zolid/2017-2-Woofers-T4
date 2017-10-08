from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login', LogInView.as_view(), name='login'),
    url(r'^auth', AuthView.as_view(), name='auth'),
]
