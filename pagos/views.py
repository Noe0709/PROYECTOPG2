from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


# Create your views here.
@login_required(login_url="login")
def display(request):
    data = models.Pago.objects.all()
    return render(request, "pago/index.html", {"data": data})


@login_required(login_url="login")
def register(request):
    if request.method == "POST":
        form = forms.PagosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pago-display")
    else:
        form = forms.PagosForm()
    return render(request, "pago/register.html", {"form": form})


@login_required(login_url="login")
def update(request, idR):
    data = models.Pago.objects.get(pago_id=idR)
    if request.method == "POST":
        form = forms.PagosForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("pago-display")
    else:
        form = forms.PagosForm(instance=data)
    return render(request, "pagoe/update.html", {"form": form})


@login_required(login_url="login")
def delete(request, idR):
    data = models.Pago.objects.get(pago_id=idR)
    if data.delete():
        return redirect("pago-display")
    else:
        return redirect("pago-display")


@login_required(login_url="login")
def counter():
    pass
