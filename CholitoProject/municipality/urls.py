from django.conf.urls import url

from municipality.views import IndexView, UserDetail

urlpatterns = [
    url(r'^user/$', UserDetail.as_view()),
    url(r'^$', IndexView.as_view(), name='municipality-index'),
]
