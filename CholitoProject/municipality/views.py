from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from CholitoProject.userManager import get_user_index
from complaint.models import Complaint


# TODO: removed PermissionRequiredMixin for now
class IndexView( LoginRequiredMixin, View):
    permission_required = 'municipality.municipal_user_access'
    template_name = 'muni_complaints_main.html'
    context = {}

    def get(self, request, **kwargs):
        c_user = get_user_index(request.user)
        self.context['complaints'] = Complaint.objects.filter(municipality=c_user.municipality)
        self.context['c_user'] = c_user
        return render(request, self.template_name, context=self.context)
