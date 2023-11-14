from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre", max_length=30, required=True, help_text='Se requieren 30 caracteres o menos.')
    last_name = forms.CharField(label="Apellido", max_length=30, required=True, help_text='Se requieren 30 caracteres o menos.')
    email = forms.EmailField(max_length=254, required=True, help_text='Introduzca una dirección de correo electrónico válida.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            Submit('register', 'Register')
        )

    
class EdicionPerfil(UserChangeForm):
    password = None
    email = forms.EmailField(label='Cambiar email', required=False)
    first_name = forms.CharField(label='Cambiar nombre', required=False)
    last_name = forms.CharField(label='Cambiar apellido', required=False)
    biografia = forms.CharField(max_length=300, required=False, widget=forms.Textarea)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'biografia', 'avatar']
