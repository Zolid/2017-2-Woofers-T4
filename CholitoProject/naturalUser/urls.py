from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^login/$', LogInView.as_view(), name='login'),
    url(r'^signup/$', SignUpView.as_view(), name='signup'),
    url(r'^$', IndexView.as_view(), name='user-index'),
    # for now
    url(r'^user-ong-in/$', OngInViewTemplate.as_view(), name='user-ong-in'),
    url(r'^user-ong-out/$', OngOutViewTemplate.as_view(), name='user-ong-out'),

]
