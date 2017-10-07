from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class LogInView(TemplateView):
    template_name = 'login.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)
