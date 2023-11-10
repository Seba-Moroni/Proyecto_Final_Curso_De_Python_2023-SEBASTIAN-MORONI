from django import forms
from ckeditor.widgets import CKEditorWidget

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, max_length=30)
    email = forms.EmailField(label="Email", required=True)
    contenido = forms.CharField(label="Contenido", widget=CKEditorWidget(), required=True)

    
