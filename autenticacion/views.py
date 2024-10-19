from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from autenticacion.forms import EditForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission


# Create your views here.
@login_required(login_url="login")
def display(request):
    data = User.objects.all()  # Obtener todos los usuarios
    permissions = Permission.objects.all()  # Carga todos los permisos
    form = EditForm(initial={"user_permissions": permissions})
    return render(request, "user/index.html", {"data": data, "form": form})


@login_required(login_url="login")
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect("user-display")  # Redirect to a user list view
    else:
        form = UserForm()
    return render(request, "user/register.html", {"form": form})


@login_required(login_url="login")
def update(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        form = EditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            # Optionally, add a success message
            return redirect("user-display")  # Redirect to the user's detail page
    else:
        form = EditForm(instance=user)

    return render(request, "user/update.html", {"form": form})


@login_required(login_url="login")
def delete(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if user.delete():
        # Optionally, add a success message
        return redirect("user-display")  # Redirect to the user's detail page
    else:
        return redirect("user-display")
