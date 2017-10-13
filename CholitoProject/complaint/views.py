from django.shortcuts import render, redirect
from django.views import View

from complaint.forms import ComplaintForm


class ComplaintView(View):
    form = ComplaintForm()
    context = {'form': form}
    template_name = 'complaint.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name, context=self.context)


class ComplaintSendView(View):
    def post(self, request, **kwargs):
        form = ComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.status = 1
            complaint.save()

        return redirect('/')
