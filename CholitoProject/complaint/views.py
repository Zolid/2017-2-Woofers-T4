from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from CholitoProject.userManager import get_user_index
from complaint.forms import ComplaintForm, ImageForm
from complaint.models import Complaint, ComplaintImage


class ComplaintView(View):
    form = ComplaintForm(prefix='complaint')
    image_form = ImageForm(prefix='image')
    context = {'form': form, 'image_form': image_form}
    template_name = 'complaint.html'

    def get(self, request, **kwargs):
        user = get_user_index(request.user)
        self.context['c_user'] = user
        return render(request, self.template_name, context=self.context)


class ComplaintSendView(PermissionRequiredMixin, LoginRequiredMixin, View):
    permission_required = 'naturalUser.natural_user_access'

    def post(self, request, **kwargs):
        form = ComplaintForm(request.POST, prefix='complaint')
        image_form = ComplaintForm(request.POST, request.FILES, prefix='image')
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.status = 1
            complaint.save()

            if image_form.is_valid():
                ComplaintImage.objects.create(complaint=complaint, image=image_form.cleaned_data.get('complaint_image'))

        return redirect('/')


class ComplaintRenderView(View):
    template_name = 'view_complaint.html'
    context = {}

    def get(self, request, pk, **kwargs):
        user = get_user_index(request.user)
        self.context['c_user'] = user
        complaint = get_object_or_404(Complaint, pk=pk)
        self.context['complaint'] = complaint

        images = ComplaintImage.objects.filter(complaint=complaint)
        self.context['images'] = images

        return render(request, self.template_name, context=self.context)
