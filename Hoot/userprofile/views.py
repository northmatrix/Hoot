# Create your views here.

from django.shortcuts import redirect, render

from .forms import RegistrationForm


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "account/login"
            )  # Redirect to login page after registration
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})
