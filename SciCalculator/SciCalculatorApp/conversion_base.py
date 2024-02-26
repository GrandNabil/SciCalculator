def decimal_to_binary(decimal):
    return bin(decimal)[2:].zfill(8)  # Ajout de zéros non significatifs pour obtenir 8 bits

def binary_to_decimal(binary):
    return int(binary, 2)

def convert_bases(number, base):
    if base == 'b':
        return (decimal_to_binary(number),)
    elif base == 'd':
        return (str(binary_to_decimal(number)),)
    elif base == 'o':
        decimal = binary_to_decimal(number)
        return (oct(decimal)[2:],)
    elif base == 'h':
        decimal = binary_to_decimal(number)
        return (hex(decimal)[2:],)
    else:
        return (number,)
