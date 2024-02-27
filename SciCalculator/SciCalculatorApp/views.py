from django.shortcuts import render
from .forms import NumberConversionForm, IPConversionForm
from .conversion_base import conversion_binaire, conversion_hexadecimal, conversion_octal
from .conversion_ip import decimal_to_binary

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
    form = IPConversionForm()
    if request.method == 'POST':
        decimal_ip = request.POST.get('decimal_ip')
        binary_ip = decimal_to_binary(decimal_ip)
        return render(request, 'conversion_ip.html', {'binary_ip': binary_ip})
    #return render(request, 'conversion_ip.html')
    return render(request, 'conversion_ip.html', {'form': form})
