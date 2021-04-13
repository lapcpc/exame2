from django import forms
from .models import Registro

class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = '__all__'
        exclude = ['timestamp_out','comment']