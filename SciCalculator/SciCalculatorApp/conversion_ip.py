def decimal_to_binary(decimal_ip):
    # Diviser l'adresse IP en octets
    octets = list(map(int, decimal_ip.split('.')))
    
    # Convertir chaque octet en binaire et le formater sur 8 bits
    binary_octets = [format(octet, '08b') for octet in octets]
    
    # Joindre les octets avec des points
    binary_ip = '.'.join(binary_octets)
    
    return binary_ip

    pass