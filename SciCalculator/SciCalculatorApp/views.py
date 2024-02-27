from django.shortcuts import render
from .forms import NumberConversionForm, IPConversionForm
from .conversion_base import conversion_binaire, conversion_hexadecimal, conversion_octal
from .conversion_ip import ip_to_binary

def home(request):
    return render(request, 'home.html')


def number_conversion(request):
    form = NumberConversionForm(request.POST or None)
    resultats = {}
    if form.is_valid():
        num = form.cleaned_data['num']
        resultats['decimal'] = num
        resultats['binaire'] = conversion_binaire(num)
        resultats['octal'] = conversion_octal(num)
        resultats['hexadecimal'] = conversion_hexadecimal(num)
    return render(request, 'conversion_base.html', {'form': form, 'resultats': resultats})

def ip_conversion(request):
    form = IPConversionForm(request.POST or None)
    ip_binaire = None
    if request.method == 'POST' and form.is_valid():
        ip_address = form.cleaned_data['ip_address']
        ip_binaire = ip_to_binary(ip_address)

    return render(request, 'conversion_ip.html', {'form': form, 'ip_binaire': ip_binaire})