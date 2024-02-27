from django.shortcuts import render
from .forms import NumberConversionForm, IPConversionForm
from .conversion_base import convert_to_binary, convert_to_octal, convert_to_hexadecimal
from .conversion_ip import decimal_to_binary

def home(request):
    return render(request, 'home.html')


def number_conversion(request):
    if request.method == 'POST':
        if request.method == 'POST':
            num = int(request.POST.get('number'))
            decimal = num
            binary = convert_to_binary(num)
            octal = convert_to_octal(num)
            hexadecimal = convert_to_hexadecimal(num)
        return render(request, 'conversion_base.html', {'decimal': decimal, 'binary': binary, 'octal': octal, 'hexadecimal': hexadecimal})
    #return render(request, 'conversion_base.html')
    return render(request, 'conversion_base.html', {'form': form})

def ip_conversion(request):
    if request.method == 'POST':
        decimal_ip = request.POST.get('decimal_ip')
        binary_ip = decimal_to_binary(decimal_ip)
        return render(request, 'conversion_ip.html', {'binary_ip': binary_ip})
    #return render(request, 'conversion_ip.html')
    return render(request, 'conversion_ip.html', {'form': form})
