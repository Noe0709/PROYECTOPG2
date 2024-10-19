from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


# Create your views here.
@login_required(login_url="login")
def display(request):
    data = models.Cliente.objects.all()
    return render(request, "cliente/index.html", {"data": data})


@login_required(login_url="login")
def register(request):
    if request.method == "POST":
        form = forms.ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("client-display")
    else:
        form = forms.ClientForm()
    return render(request, "cliente/register.html", {"form": form})


@login_required(login_url="login")
def update(request, idR):
    data = models.Cliente.objects.get(id=idR)
    if request.method == "POST":
        form = forms.ClientForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("client-display")
    else:
        form = forms.ClientForm(instance=data)
    return render(request, "cliente/update.html", {"form": form})


@login_required(login_url="login")
def delete(request, idR):
    data = models.Cliente.objects.get(id=idR)
    if data.delete():
        return redirect("client-display")
    else:
        return redirect("client-display")


@login_required(login_url="login")
def counter():
    pass
