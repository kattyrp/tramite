#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from documento.models import Documento_generado

class DocumentoForm(ModelForm):
    class Meta:
        model = Documento_generado