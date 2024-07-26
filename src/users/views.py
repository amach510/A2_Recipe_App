from django.shortcuts import render
from .models import User
from django.views.generic import DetailView


# Create your views here.
def profile(request):
    user = User.objects.first()  # Retrieve the first user
    context = {"user": user}
    return render(request, "users/users_profile.html", context)


class profile(DetailView):
    model: User
    template_name = "users/users_profile.html"
    context_object_name = "current_user"

    def get_object(self, queryset=None):
        return self.request.user
