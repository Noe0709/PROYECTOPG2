from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


# Create your views here.
@login_required(login_url="login")
def display(request):
    data = models.Poliza.objects.all()
    return render(request, "poliza/index.html", {"data": data})


@login_required(login_url="login")
def register(request):
    if request.method == "POST":
        form = forms.PolizaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("poliza-display")
    else:
        form = forms.PolizaForm()
    return render(request, "poliza/register.html", {"form": form})


@login_required(login_url="login")
def update(request, idR):
    data = models.Poliza.objects.get(no_poliza=idR)
    if request.method == "POST":
        form = forms.PolizaUpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("poliza-display")
    else:
        form = forms.PolizaUpdateForm(instance=data)
    return render(request, "poliza/update.html", {"form": form})


@login_required(login_url="login")
def delete(request, idR):
    data = models.Poliza.objects.get(no_poliza=idR)
    if data.delete():
        return redirect("poliza-display")
    else:
        return redirect("poliza-display")


@login_required(login_url="login")
def counter():
    pass
