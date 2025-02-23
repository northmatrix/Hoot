from django.shortcuts import redirect, render

from .forms import CustomUserCreationForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "/account/login"
            )  # Redirect to login page after registration
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form})
