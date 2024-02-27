from django import forms

class NumberConversionForm(forms.Form):
    CHOICES = [('d', 'Décimal'), ('b', 'Binaire'), ('o', 'Octal'), ('h', 'Hexadécimal')]
    number = forms.CharField(label="Nombre", required=False)
    base = forms.ChoiceField(label="Base", choices=CHOICES)
    decimal_result = forms.CharField(label="Décimal", required=False)
    binary_result = forms.CharField(label="Binaire", required=False)
    octal_result = forms.CharField(label="Octal", required=False)
    hexadecimal_result = forms.CharField(label="Hexadécimal", required=False)

class IPConversionForm(forms.Form):
    ip_decimal = forms.CharField(label="Adresse IP Décimale", required=False)
    ip_binary = forms.CharField(label="Adresse IP Binaire", required=False)
