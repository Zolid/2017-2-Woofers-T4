from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from CholitoProject.userManager import get_user_index
from complaint.models import AnimalType
from naturalUser.forms import SignUpForm, AvatarForm
from naturalUser.models import NaturalUser


class IndexView(TemplateView):
    context = {}

    def get(self, request, **kwargs):
        c_user = get_user_index(request.user)
        self.context['c_user'] = c_user
        animals = AnimalType.objects.all()
        if c_user is None:
            return render(request, 'index.html', {'animals': animals})
        self.context['animals'] = animals
        return c_user.get_index(request, self.context)


class LogInView(TemplateView):
    template_name = 'login.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)


class SignUpView(View):
    user_form = SignUpForm(initial={'username': 'dummy'}, prefix='user')
    avatar_form = AvatarForm(prefix='avatar')
    context = {'user_form': user_form, 'avatar_form': avatar_form}
    template_name = 'sign_up.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.context)

    def post(self, request, **kwargs):
        user_form = SignUpForm(request.POST, prefix='user')
        avatar_form = AvatarForm(request.POST, request.FILES, prefix='avatar')
        if user_form.is_valid() and avatar_form.is_valid():
            user_ = user_form.save()
            user_.refresh_from_db()
            natural_user = NaturalUser.objects.create(user=user_, avatar=avatar_form.cleaned_data.get('avatar'))
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
