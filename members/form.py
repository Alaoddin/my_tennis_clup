
from django import forms
from .models import Mabani
from django import forms



# class MyForm(BootstrapForm):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()


class EstateForm(forms.ModelForm):
    class Meta:
        model = Mabani
        fields = ['name','prise','adress','city','estate_type']
        
    