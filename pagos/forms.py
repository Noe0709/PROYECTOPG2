from django import forms
from . import models


class PagosForm(forms.ModelForm):
    class Meta:
        model = models.Pago
        fields = "__all__"


class PagosUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["pago_id"].widget.attrs["readonly"] = True

    class Meta:
        model = models.Pago
        fields = "__all__"
