from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from CholitoProject.userManager import get_user_index
from naturalUser.forms import SignUpForm
from naturalUser.models import NaturalUser


class IndexView(TemplateView):

    def get(self, request, **kwargs):
        c_user = get_user_index(request.user)
        if c_user is None:
            return render(request, 'index.html')
        return c_user.get_index(request, {"c_user": c_user})


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
        print(user_form.is_valid())
        if user_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()
            natural_user = NaturalUser.objects.create(user=user)
            username = user_form.cleaned_data.get('email')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return natural_user.get_index(request)
        return render(request, self.template_name, context=self.context)


class OngInViewTemplate(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    permission_required = 'naturalUser.natural_user_access'
    template_name = 'usuario-in-ong.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)


class OngOutViewTemplate(TemplateView):
    template_name = 'usuario-out-ong.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)
