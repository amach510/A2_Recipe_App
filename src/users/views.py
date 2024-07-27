from django.shortcuts import render
from .models import User
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def profile(request):
    user = User.objects.first()  # Retrieve the first user
    context = {"user": user}
    return render(request, "users/users_profile.html", context)


class profile(LoginRequiredMixin, DetailView):
    model: User
    template_name = "users/users_profile.html"
    context_object_name = "current_user"

    def get_object(self, queryset=None):
        return self.request.user
