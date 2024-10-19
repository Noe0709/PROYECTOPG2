from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


# Create your views here.
@login_required(login_url="login")
def display(request):
    data = models.Producto.objects.all()
    return render(request, "productos/index.html", {"data": data})


@login_required(login_url="login")
def register(request):
    if request.method == "POST":
        form = forms.ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product-display")
    else:
        form = forms.ProductForm()
    return render(request, "productos/register.html", {"form": form})


@login_required(login_url="login")
def update(request, idR):
    data = models.Producto.objects.get(producto_cod=idR)
    if request.method == "POST":
        form = forms.ProductUpdateForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("product-display")
    else:
        form = forms.ProductUpdateForm(instance=data)
    return render(request, "productos/update.html", {"form": form})


@login_required(login_url="login")
def delete(request, idR):
    data = models.Producto.objects.get(producto_cod=idR)
    if data.delete():
        return redirect("product-display")
    else:
        return redirect("product-display")


@login_required(login_url="login")
def counter():
    pass
