from django import forms
from . import models


class IndicadorForm(forms.ModelForm):
    class Meta:
        model = models.Indicador
        fields = "__all__"


class IndicadorUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["id_ci"].widget.attrs["readonly"] = True

    class Meta:
        model = models.Indicador
        fields = "__all__"
