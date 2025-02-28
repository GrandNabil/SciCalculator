import re
def ip_to_binary(ip_address):
    try:
        # Vérifier que nous avons bien 4 octets
        ip_octets = ip_address.split('.')
        if len(ip_octets) != 4:
            raise ValueError("L'adresse IP doit contenir exactement 4 octets")

        # Convertir chaque octet en binaire et vérifier qu'il est dans la plage valide (0-255)
        binary_octets = []
        for octet in ip_octets:
            octet_value = int(octet)
            if octet_value < 0 or octet_value > 255:
                raise ValueError(f"Octet invalide: {octet} - doit être entre 0 et 255")
            # Convertir en binaire, supprimer le préfixe '0b' et remplir avec des 0 à gauche pour avoir 8 bits
            binary_octet = bin(octet_value)[2:].zfill(8)
            binary_octets.append(binary_octet)

        # Joindre les octets avec des points
        ip_binary = '.'.join(binary_octets)
        return ip_binary

    except ValueError as e:
        # Re-lever l'exception avec un message plus descriptif
        raise ValueError(f"Adresse IP invalide '{ip_address}': {str(e)}")
    except Exception as e:
        # Capturer toute autre exception
        raise ValueError(f"Erreur lors de la conversion de l'adresse IP '{ip_address}': {str(e)}")

def validate_ip(ip_address):
    """Valide l'adresse IP."""
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    return pattern.match(ip_address) is not None