from django.shortcuts import render, get_object_or_404
from django.views import View

from CholitoProject.userManager import get_user_index
from animals.models import Animal, Adopt
from complaint.models import AnimalType
from naturalUser.models import NaturalUser


class AnimalRenderView(View):
    template_name = 'view_animal.html'
    context = {'animals': AnimalType.objects.all()}

    def get(self, request, pk, **kwargs):
        c_user = get_user_index(request.user)
        self.context['c_user'] = c_user

        animal = get_object_or_404(Animal, pk=pk)
        adopt_users_pk = Adopt.objects.filter(animal=animal).values('user')
        adopt_users = list(NaturalUser.objects.filter(pk__in=adopt_users_pk))
        self.context['selected_animal'] = animal
        self.context['adopters'] = adopt_users
        self.context['adopt_selected'] = c_user in adopt_users
        return render(request, self.template_name, context=self.context)
