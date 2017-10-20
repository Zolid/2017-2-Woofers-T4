from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from naturalUser.forms import SignUpForm
from naturalUser.models import NaturalUser


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)


class LogInView(TemplateView):
    template_name = 'login.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)


class SignUpView(View):
    form = SignUpForm({'username': 'dummy'})
    context = {'form': form}
    template_name = 'sign_up.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.context)

    def post(self, request, **kwargs):
        user_form = SignUpForm(request.POST)
        print(user_form)
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            natural_user = NaturalUser.objects.create(user=user)
            username = user_form.cleaned_data.get('email')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return natural_user.get_index()
        return render(request, self.template_name, context=self.context)
