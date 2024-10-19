from django import forms
from . import models


class ReclamoForm(forms.ModelForm):

    class Meta:
        model = models.Reclamo
        fields = "__all__"


class ReclamoUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["no_incidente"].widget.attrs["readonly"] = True

    class Meta:
        model = models.Reclamo
        fields = "__all__"



