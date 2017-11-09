from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin,\
    LoginRequiredMixin
from complaint.models import Complaint
from CholitoProject.userManager import get_user_index


class IndexView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'municipality.municipality_user_access'
    template_name = 'muni_complaints_main.html'
    context = {}

    def getComplaintStats(self, complaints):
        stats_complaint = {}
        status_parser = dict(Complaint().COMPLAINT_STATUS)

        for key, value in status_parser.items():
            stats_complaint[value] = 0

        for complaint in list(complaints):
            temp_status = status_parser.get(complaint.status)
            stats_complaint[temp_status] += 1

        return stats_complaint

    def get(self, request, **kwargs):
        user = get_user_index(request.user)
        complaints = Complaint.objects.filter(
            municipality=user.municipality)

        self.context['complaints'] = complaints
        self.context['c_user'] = user
        self.context['stats'] = self.getComplaintStats(complaints)
        return render(request, self.template_name, context=self.context)


class StatisticsView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'municipality.municipality_user_access'
    template_name = 'muni_statistics.html'
    context = {}

    def get(self, request, **kwargs):
        user = get_user_index(request.user)
        self.context['c_user'] = user
        return render(request, self.template_name, context=self.context)


class UserDetail(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'municipality.municipality_user_access'

    def post(self, request, **kwargs):
        c_user = get_user_index(request.user)
        if 'avatar' in request.FILES:
            c_user.municipality.avatar = request.FILES['avatar']
            c_user.municipality.save()
        return redirect('/')
