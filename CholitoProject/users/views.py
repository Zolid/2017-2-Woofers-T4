from django.contrib import auth
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)


class LogInView(TemplateView):
    template_name = 'login.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)


# TODO: redirect to correct template
class AuthView(View):
    def post(self, request, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)

        # TODO: error logging in
        if user is None:
            return redirect('/login')

        if user.is_active:
            auth.login(request, user)
            return redirect('/')

        # TODO: deleted user
        return redirect('/login')
