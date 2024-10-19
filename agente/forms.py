from django import forms
from . import models


class AgenteForm(forms.ModelForm):
    class Meta:
        model = models.Agente
        fields = "__all__"


class AgenteUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["no_empleado"].widget.attrs["readonly"] = True

    class Meta:
        model = models.Agente
        fields = "__all__"
