from django import forms
from . import models


class ClientForm(forms.ModelForm):
    nombre = forms.CharField(
        required=True,
        label="nombre",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "nombre"}
        ),
    )
    email = forms.EmailField(
        required=True,
        label="email",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "email"}),
    )
    telefono = forms.CharField(
        required=True,
        label="telefono",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "telefono"}
        ),
    )
    direccion = forms.CharField(
        required=True,
        label="direccion",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "direccion"}
        ),
    )

    class Meta:
        model = models.Cliente
        fields = "__all__"
