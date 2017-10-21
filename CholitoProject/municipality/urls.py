from django.conf.urls import url

from municipality.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='municipality-index'),
]
