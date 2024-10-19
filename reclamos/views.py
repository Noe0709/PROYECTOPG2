from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


# Create your views here.
@login_required(login_url="login")
def display(request):
    data = models.Reclamo.objects.all()
    return render(request, "reclamo/index.html", {"data": data})


@login_required(login_url="login")
def register(request):
    if request.method == "POST":
        form = forms.ReclamoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reclamo-display")
    else:
        form = forms.ReclamoForm()
    return render(request, "reclamo/register.html", {"form": form})


@login_required(login_url="login")
def update(request, idR):
    data = models.Reclamo.objects.get(no_incidente=idR)
    if request.method == "POST":
        form = forms.ReclamoUpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("reclamo-display")
    else:
        form = forms.ReclamoUpdateForm(instance=data)
    return render(request, "reclamo/update.html", {"form": form})


@login_required(login_url="login")
def delete(request, idR):
    data = models.Reclamo.objects.get(no_incidente=idR)
    if data.delete():
        return redirect("reclamo-display")
    else:
        return redirect("reclamo-display")


@login_required(login_url="login")
def counter():
    pass
