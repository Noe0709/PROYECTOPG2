from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


# Create your views here.
@login_required(login_url="login")
def display(request):
    data = models.Indicador.objects.all()
    return render(request, "indicador/index.html", {"data": data})


@login_required(login_url="login")
def register(request):
    if request.method == "POST":
        form = forms.IndicadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("indicador-display")
    else:
        form = forms.IndicadorForm()
    return render(request, "indicador/register.html", {"form": form})


@login_required(login_url="login")
def update(request, idR):
    data = models.Indicador.objects.get(id_ci=idR)
    if request.method == "POST":
        form = forms.IndicadorUpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("indicador-display")
    else:
        form = forms.IndicadorUpdateForm(instance=data)
    return render(request, "indicador/update.html", {"form": form})


@login_required(login_url="login")
def delete(request, idR):
    data = models.Indicador.objects.get(id_ci=idR)
    if data.delete():
        return redirect("indicador-display")
    else:
        return redirect("indicador-display")


@login_required(login_url="login")
def counter():
    pass
