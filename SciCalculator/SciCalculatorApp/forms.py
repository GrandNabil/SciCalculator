from django import forms

class NumberConversionForm(forms.Form):
    CHOICES = [('d', 'Décimal'), ('b', 'Binaire'), ('o', 'Octal'), ('h', 'Hexadécimal')]
    number = forms.CharField(label="Nombre", required=False)
    base = forms.ChoiceField(label="Base", choices=CHOICES)
    decimal_result = forms.CharField(label="Décimal", required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    binary_result = forms.CharField(label="Binaire", required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    octal_result = forms.CharField(label="Octal", required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    hexadecimal_result = forms.CharField(label="Hexadécimal", required=False, widget=forms.TextInput(attrs={'readonly': 'readonly'}))

class IPConversionForm(forms.Form):
    ip_decimal = forms.CharField(label="Adresse IP Décimale", required=False)
    ip_binary = forms.CharField(label="Adresse IP Binaire", required=False)
