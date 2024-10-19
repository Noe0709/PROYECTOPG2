from django import forms
from . import models


class SiniestroForm(forms.ModelForm):

    class Meta:
        model = models.Siniestro
        fields = "__all__"


class SiniestroUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["id_siniestro"].widget.attrs["readonly"] = True

    class Meta:
        model = models.Siniestro
        fields = "__all__"
