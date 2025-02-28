from django.shortcuts import render
from .forms import NumberConversionForm, IPConversionForm
from .conversion_base import conversion_bases
from .conversion_ip import ip_to_binary, validate_ip


def home(request):
    return render(request, 'home.html')


def number_conversion(request):
    # Initialiser les résultats comme vide
    resultats = {}
    error_message = None

    # Traiter le formulaire s'il est soumis
    if request.method == 'POST':
        form = NumberConversionForm(request.POST)
        if form.is_valid():
            try:
                # Récupérer les données du formulaire
                nombre = form.cleaned_data['num']
                base = form.cleaned_data.get('base', 10)  # Récupérer la base avec une valeur par défaut de 10

                # Vérifier que la base est valide
                if base not in [2, 8, 10, 16]:
                    error_message = "Base non supportée. Veuillez entrer 2, 8, 10 ou 16."
                else:
                    # Effectuer la conversion
                    resultats = conversion_bases(nombre, base)
            except ValueError:
                error_message = "Erreur: entrée invalide pour la base spécifiée."
            except Exception as e:
                error_message = f"Une erreur s'est produite: {str(e)}"
    else:
        form = NumberConversionForm()

    # Rendre le template avec le contexte
    context = {
        'form': form,
        'resultats': resultats,
        'error_message': error_message
    }

    return render(request, 'conversion_base.html', context)

def ip_conversion(request):
    # Initialiser les résultats comme vide
    ip_binaire = None
    error_message = None

    # Traiter le formulaire s'il est soumis
    if request.method == 'POST':
        form = IPConversionForm(request.POST)
        if form.is_valid():
            try:
                # Récupérer l'adresse IP du formulaire
                ip_address = form.cleaned_data['ip_address']

                # Valider l'adresse IP
                if not validate_ip(ip_address):
                    error_message = "Adresse IP invalide. Veuillez entrer une adresse IP valide (ex: 192.168.1.1)."
                else:
                    # Convertir l'adresse IP en binaire
                    ip_binaire = ip_to_binary(ip_address)
            except ValueError as e:
                error_message = f"Erreur lors de la conversion : {str(e)}"
            except Exception as e:
                error_message = f"Une erreur s'est produite : {str(e)}"
    else:
        form = IPConversionForm()

    # Rendre le template avec le contexte
    context = {
        'form': form,
        'ip_binaire': ip_binaire,
        'error_message': error_message
    }

    return render(request, 'conversion_ip.html', context)