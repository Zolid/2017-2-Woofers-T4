from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin,\
    LoginRequiredMixin
from complaint.models import Complaint
from municipality.models import MunicipalityUser
from CholitoProject.userManager import get_user_index


def check_permissions(request, request_profile):
    actual_user = MunicipalityUser.objects.get(user=request.user)
    return actual_user == request_profile


class IndexView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'municipality.municipality_user_access'
    template_name = 'muni_complaints_main.html'
    context = {}

    def get(self, request, **kwargs):
        # .filter(municipality=user.municipality)
        self.context['complaints'] = Complaint.objects.all()
        self.context['c_user'] = get_user_index(request.user)
        return render(request, self.template_name, context=self.context)
