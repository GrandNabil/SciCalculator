def decimal_to_binary(decimal):
    return bin(decimal)[2:].zfill(8)  # Ajout de zéros non significatifs pour obtenir 8 bits

def binary_to_decimal(binary):
    return int(binary, 2)

def ipv4_decimal_to_binary(ipv4_decimal):
    octets = ipv4_decimal.split('.')
    binary_octets = [decimal_to_binary(int(octet)) for octet in octets]
    return '.'.join(binary_octets)

def ipv4_binary_to_decimal(ipv4_binary):
    binary_octets = ipv4_binary.split('.')
    decimal_octets = [str(binary_to_decimal(octet)) for octet in binary_octets]
    return '.'.join(decimal_octets)
