from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


# Create your views here.
@login_required(login_url="login")
def display(request):
    data = models.Siniestro.objects.all()
    return render(request, "siniestro/index.html", {"data": data})


@login_required(login_url="login")
def register(request):
    if request.method == "POST":
        form = forms.SiniestroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("siniestro-display")
    else:
        form = forms.SiniestroForm()
    return render(request, "siniestro/register.html", {"form": form})


@login_required(login_url="login")
def update(request, idR):
    data = models.Siniestro.objects.get(id_siniestro=idR)
    if request.method == "POST":
        form = forms.SiniestroUpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("siniestro-display")
    else:
        form = forms.SiniestroUpdateForm(instance=data)
    return render(request, "siniestro/update.html", {"form": form})


@login_required(login_url="login")
def delete(request, idR):
    data = models.Siniestro.objects.get(id_siniestro=idR)
    if data.delete():
        return redirect("siniestro-display")
    else:
        return redirect("siniestro-display")


@login_required(login_url="login")
def counter():
    pass
