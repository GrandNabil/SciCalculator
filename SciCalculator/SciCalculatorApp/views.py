from django.shortcuts import render
from .forms import NumberConversionForm, IPConversionForm
from .conversion_base import convert_bases
from .conversion_ip import ipv4_decimal_to_binary, ipv4_binary_to_decimal

def home(request):
    return render(request, 'home.html')


def number_conversion(request):
    if request.method == 'POST':
        form = NumberConversionForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            base = form.cleaned_data['base']
            converted_numbers = convert_bases(number, base)
            return render(request, 'number_conversion.html', {'form': form, 'converted_numbers': converted_numbers})
    else:
        form = NumberConversionForm()
    return render(request, 'number_conversion.html', {'form': form})

def ip_conversion(request):
    if request.method == 'POST':
        form = IPConversionForm(request.POST)
        if form.is_valid():
            ip_input = form.cleaned_data['ip_input']
            ip_type = form.cleaned_data['ip_type']
            if ip_type == 'decimal':
                converted_ip = ipv4_decimal_to_binary(ip_input)
                conversion_result = f"Adresse IPv4 décimale {ip_input} convertie en binaire: {converted_ip}"
            elif ip_type == 'binary':
                converted_ip = ipv4_binary_to_decimal(ip_input)
                conversion_result = f"Adresse IPv4 binaire {ip_input} convertie en décimal: {converted_ip}"
            else:
                conversion_result = "Type d'adresse IP non reconnu."
            return render(request, 'ip_conversion.html', {'form': form, 'conversion_result': conversion_result})
    else:
        form = IPConversionForm()
    return render(request, 'ip_conversion.html', {'form': form})
