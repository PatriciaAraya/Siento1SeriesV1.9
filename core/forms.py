from django import forms
from django.forms import ModelForm, fields
from .models import Series

class SeriesForm(ModelForm):
    class Meta:
        model = Series
        fields = ['nombre', 'genero', 'imagen','sinopsis','desarrollo','controversias', 'plataforma']

