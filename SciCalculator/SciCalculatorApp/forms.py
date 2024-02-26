from django import forms


class ConversionForm(forms.Form):
    CHOICES = [('d', 'Décimal'), ('b', 'Binaire'), ('o', 'Octal'), ('h', 'Hexadécimal'), ('ip', 'Adresse IP')]
    number = forms.CharField(label="Nombre")
    base = forms.ChoiceField(label="Base", choices=CHOICES)
    ip_input = forms.CharField(label="Adresse IP", required=False)
    IP_CHOICES = [('decimal', 'Décimale'), ('binary', 'Binaire')]
    ip_type = forms.ChoiceField(label="Type d'adresse IP", choices=IP_CHOICES, required=False)
