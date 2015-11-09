from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render

from .models import Profile


def index(request):
    context = dict(profiles=Profile.objects.all())
    return render(request, 'profile/index.html', context)

def profile(request, username):
    user = get_object_or_404(User, username=username)
    context = dict(profile=user.profile)
    return render(request, 'profile/profile.html', context)
