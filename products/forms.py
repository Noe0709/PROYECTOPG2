from django import forms
from . import models


class ProductForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = "__all__"


class ProductUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["producto_cod"].widget.attrs["readonly"] = True

    class Meta:
        model = models.Producto
        fields = "__all__"
