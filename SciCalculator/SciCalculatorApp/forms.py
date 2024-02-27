from django import forms

class NumberConversionForm(forms.Form):

    num = forms.IntegerField(label="Entrez le nombre à convertir:")

class IPConversionForm(forms.Form):
    
    ip_address = forms.CharField(label='Entrez l\'adresse IP')
