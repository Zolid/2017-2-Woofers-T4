from django.shortcuts import render, get_object_or_404
from django.views import View

from animals.models import Animal


class AnimalRenderView(View):
    template_name = 'view_animal.html'
    context = {}

    def get(self, request, pk, **kwargs):
        animal = get_object_or_404(Animal, pk=pk)
        self.context['animal'] = animal
        return render(request, self.template_name, context=self.context)