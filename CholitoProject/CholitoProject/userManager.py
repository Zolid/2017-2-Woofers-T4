from municipality.models import MunicipalityUser
from naturalUser.models import NaturalUser


def get_user_index(user):
    original_user = NaturalUser.objects.get(user=user)
    if original_user is not None:
        return original_user
    original_user = MunicipalityUser.objects.get(user=user)
    if original_user is not None:
        return original_user
    else:
        return None
