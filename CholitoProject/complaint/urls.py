from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', ComplaintView.as_view(), name='complaint-form'),
    url(r'^send', ComplaintSendView.as_view(), name='make-complaint'),
]
