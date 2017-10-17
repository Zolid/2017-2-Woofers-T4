from django.conf.urls import url

from animals.views import AnimalRenderView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', AnimalRenderView.as_view(), name='see-animal')
]