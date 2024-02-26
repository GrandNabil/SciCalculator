from django.shortcuts import render
from .forms import ConversionForm
from .outils import *

def home(request):
    if request.method == 'POST':
        form = ConversionForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            base = form.cleaned_data['base']
            if base == 'ip':
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
                return render(request, 'conversion/home.html', {'form': form, 'conversion_result': conversion_result})
            else:
                converted_numbers = convert_bases(number, base)
                return render(request, 'conversion/home.html', {'form': form, 'converted_numbers': converted_numbers})
    else:
        form = ConversionForm()
    return render(request, 'conversion/home.html', {'form': form})