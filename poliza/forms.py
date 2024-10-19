from django import forms
from . import models


class PolizaForm(forms.ModelForm):

    class Meta:
        model = models.Poliza
        fields = "__all__"


class PolizaUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["no_poliza"].widget.attrs["readonly"] = True

    class Meta:
        model = models.Poliza
        fields = "__all__"
