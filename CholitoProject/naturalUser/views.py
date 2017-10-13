from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)


class LogInView(TemplateView):
    template_name = 'login.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)
