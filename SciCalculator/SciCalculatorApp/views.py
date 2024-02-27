from django.shortcuts import render
from .forms import NumberConversionForm, IPConversionForm
from .conversion_base import convert_to_binary, convert_to_octal, convert_to_hexadecimal
from .conversion_ip import decimal_to_binary

def home(request):
    return render(request, 'home.html')


def number_conversion(request):
    form = NumberConversionForm(request.POST or None)
    resultats = {}
    if form.is_valid():
        nombre = form.cleaned_data['nombre']
        resultats['decimal'] = nombre
        resultats['binaire'] = convertir_en_binaire(nombre)
        resultats['octal'] = convertir_en_octal(nombre)
        resultats['hexadecimal'] = convertir_en_hexadecimal(nombre)
    return render(request, 'conversion_base.html', {'form': form})

def ip_conversion(request):
    form = IPConversionForm()
    if request.method == 'POST':
        decimal_ip = request.POST.get('decimal_ip')
        binary_ip = decimal_to_binary(decimal_ip)
        return render(request, 'conversion_ip.html', {'binary_ip': binary_ip})
    #return render(request, 'conversion_ip.html')
    return render(request, 'conversion_ip.html', {'form': form})
