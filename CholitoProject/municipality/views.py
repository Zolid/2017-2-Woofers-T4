from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from municipality.models import MunicipalityUser


def check_permissions(request, request_profile):
    actual_user = MunicipalityUser.objects.get(user=request.user)
    return actual_user == request_profile


class IndexView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'municipality.municipal_user_access'
    template_name = 'muni-estadisticas-ongs.html'
    context = {}

    def get(self, request, pk, **kwargs):
        user = MunicipalityUser.objects.get(id=pk)
        if check_permissions(request, user):
            self.context['municipality_user'] = user
            return render(request, self.template_name, context=self.context)
        # TODO: redirect to correct index
        return redirect("/")
