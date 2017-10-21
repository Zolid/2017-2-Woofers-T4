from django.shortcuts import render
from django.views.generic import TemplateView
from CholitoProject.userManager import get_user_index


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        c_user = get_user_index(request.user)
        return render(request, self.template_name, context={"c_user": c_user})


class LogInView(TemplateView):
    template_name = 'login.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)
