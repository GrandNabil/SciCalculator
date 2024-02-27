def ip_to_binary(ip_address):
    ip_octets = ip_address.split('.')  # Séparer l'adresse IP en octets
    ip_binary = '.'.join([bin(int(octet))[2:].zfill(8) for octet in ip_octets])  # Convertir chaque octet en binaire
    return ip_binary