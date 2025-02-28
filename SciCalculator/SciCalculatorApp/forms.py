from django import forms

class NumberConversionForm(forms.Form):

    num = forms.IntegerField(label="Entrez le nombre à convertir:")

class IPConversionForm(forms.Form):
    
    ip_address = forms.CharField(label='Entrez l\'adresse IP')

num = forms.CharField(
    label='Nombre à convertir',
    max_length=100,
    required=True,
    widget=forms.TextInput(attrs={'class': 'form-control'})
)
base = forms.ChoiceField(
    label='Base d\'entrée',
    choices=[
        (10, 'Décimal'),
        (2, 'Binaire'),
        (8, 'Octal'),
        (16, 'Hexadécimal')
    ],
    initial=10,
    required=True,
    widget=forms.Select(attrs={'class': 'form-control'})
)