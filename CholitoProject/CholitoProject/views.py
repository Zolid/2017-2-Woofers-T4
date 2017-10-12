from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from CholitoProject.userManager import get_user_index
from django.shortcuts import redirect


def home(request):
    return redirect('user-home')


# TODO: redirect to correct template
class AuthView(View):

    def post(self, request, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            current_user = get_user_index(user)
            print(current_user)
            if current_user is not None:
                login(request, user)
                return current_user.get_index()

        # TODO: no user
        raise Http404("No user found")


class LogOutView(View):

    def get(self, request, **kwargs):
        logout(request)
        return redirect('/')
