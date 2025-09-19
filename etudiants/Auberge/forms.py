from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import Etudiant, Etage, Auberge, TypeChambre, Chambre, Habiter, CustomUser





class Form_Etudiant(forms.ModelForm):
    class Meta:
        model= Etudiant
        fields='__all__'
class Form_Etage(forms.ModelForm):
    class Meta:
        model= Etage
        fields= '__all__'

class FormAUberge(forms.ModelForm):
    nombreEtage=forms.IntegerField(max_value=20)
    class Meta:
        model= Auberge
        fields=['adresseAuberge','nomAuberge','nombreEtage', 'description']
class FormTypeChambre(forms.ModelForm):
    nombeTypeChambre= forms.IntegerField(max_value=12)
    class Meta:
        model=TypeChambre
        fields= '__all__'
class FormChambre(forms.ModelForm):
    nombreChambre=forms.IntegerField(max_value=1000)
    class Meta:
        model= Chambre
        fields='__all__'
class FormHabiter(forms.ModelForm):
    class Meta:
        model= Habiter
        fields='__all__'
class Form_Login(UserCreationForm):
    password1 = forms.CharField(
        label="Mot de passe", required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none '
                     'focus:ring-3 focus:ring-blue-200 focus:border-blue-500'
        })
    )
    password2 = forms.CharField(
        label="Confirmation mot de passe", required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none '
                     'focus:ring-3 focus:ring-blue-200 focus:border-blue-500'
        })
    )
    class Meta:
        model=CustomUser
        fields=("username","first_name","last_name","email","password1","password2")

        
        help_texts = {
            "username": None,
            "email": None,
            "password1": None,
            "password2": None,
        }
       
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password")
       
    
class user_cerateForm(forms.ModelForm):
    username = forms.CharField(
        label="username", required=False,
        widget=forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none '
                     'focus:ring-3 focus:ring-blue-200 focus:border-blue-500'
        })
    )
    class Meta:
        model=CustomUser
        fields = ('username','first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none '
                         'focus:ring-3 focus:ring-blue-200 focus:border-blue-500'
            }),
            'username': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none '
                         'focus:ring-3 focus:ring-blue-200 focus:border-blue-500'
            }),
           
            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none '
                         'focus:ring-3 focus:ring-blue-200 focus:border-blue-500'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none '
                         'focus:ring-3 focus:ring-blue-200 focus:border-blue-500'
            }),
          
        }