from django import forms

class NumberConversionForm(forms.Form):

    number = forms.IntegerField(label="Entrez le nombre à convertir:")

class IPConversionForm(forms.Form):
    ip_decimal = forms.CharField(label="Adresse IP Décimale", required=False)
    ip_binary = forms.CharField(label="Adresse IP Binaire", required=False)
