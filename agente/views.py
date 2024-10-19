from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


# Create your views here.
@login_required(login_url="login")
def display(request):
    data = models.Agente.objects.all()
    return render(request, "agente/index.html", {"data": data})


@login_required(login_url="login")
def register(request):
    if request.method == "POST":
        form = forms.AgenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("agente-display")
    else:
        form = forms.AgenteForm()
    return render(request, "agente/register.html", {"form": form})


@login_required(login_url="login")
def update(request, idR):
    data = models.Agente.objects.get(no_empleado=idR)
    if request.method == "POST":
        form = forms.AgenteForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("agente-display")
    else:
        form = forms.AgenteForm(instance=data)
    return render(request, "agente/update.html", {"form": form})


@login_required(login_url="login")
def delete(request, idR):
    data = models.Agente.objects.get(no_empleado=idR)
    if data.delete():
        return redirect("agente-display")
    else:
        return redirect("agente-display")


@login_required(login_url="login")
def counter():
    pass
