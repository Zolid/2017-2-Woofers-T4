from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from municipality.views import IndexView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', login_required(IndexView.as_view()), name='municipality-index'),
]
