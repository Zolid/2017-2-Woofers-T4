from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404
from django.views import View

from animals.models import Animal, Adopt
from naturalUser.models import NaturalUser


# TODO: ONG can see this pago too
def is_adopt_selected(request, adopt_users):
    try:
        natural_user = NaturalUser.objects.get(user=request.user)
    except ObjectDoesNotExist:
        return False
    return natural_user in adopt_users


class AnimalRenderView(View):
    template_name = 'view_animal.html'
    context = {}

    def get(self, request, pk, **kwargs):
        animal = get_object_or_404(Animal, pk=pk)
        adopt_users_pk = Adopt.objects.filter(animal=animal).values('user')
        adopt_users = list(NaturalUser.objects.filter(pk__in=adopt_users_pk))
        self.context['animal'] = animal
        self.context['adopters'] = adopt_users
        self.context['adopt_selected'] = is_adopt_selected(request, adopt_users)
        return render(request, self.template_name, context=self.context)
