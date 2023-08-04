from django import forms
from .models import Con


class contact1(forms.ModelForm):
    class Meta:
        model = Con
        fields = '__all__'
        widgets = {'name' : forms.TextInput(attrs={'class' : 'form-control'}) ,
                   'email': forms.EmailInput(attrs={'class': 'form-control'}) ,
                   'subject': forms.TextInput(attrs={'class': 'form-control'}) ,
                   'message': forms.TextInput(attrs={'class': 'form-control'})
                   }
