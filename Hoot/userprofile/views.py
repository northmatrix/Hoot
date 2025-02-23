# Create your views here.

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import UserProfile


@login_required
def profile(request):
    if request.method == "GET":
        user = request.user
        profile = {
            "profile_picture_url": user.profile.profile_picture.url,
            "bio": user.profile.bio,
        }
        return render(
            request,
            "profile.html",
            {"user": user, "profile": profile},
        )
