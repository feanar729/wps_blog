from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        auth_logout(request)
        return redirect(reverse("home"))
