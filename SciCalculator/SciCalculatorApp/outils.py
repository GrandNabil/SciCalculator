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

def main():
    number = input("Entrez un nombre : ")
    base = input("Entrez la base du nombre (d/b/o/h pour décimal/binaire/octal/hexadécimal, i pour adresse IPv4) : ").lower()

    if base in ['b', 'd', 'o', 'h']:
        converted_numbers = convert_bases(number, base)
        print(f"Conversion de {number} en base {base}:")
        for idx, value in enumerate(converted_numbers):
            print(f"Base {['Décimal', 'Binaire', 'Octal', 'Hexadécimal'][idx]}: {value}")
    elif base == 'i':
        is_decimal = input("Entrez 'd' si c'est une adresse IPv4 décimale ou 'b' si c'est une adresse IPv4 binaire : ").lower()
        if is_decimal == 'd':
            converted_ip = ipv4_decimal_to_binary(number)
            print(f"Adresse IPv4 décimale {number} convertie en binaire: {converted_ip}")
        elif is_decimal == 'b':
            converted_ip = ipv4_binary_to_decimal(number)
            print(f"Adresse IPv4 binaire {number} convertie en décimal: {converted_ip}")
        else:
            print("Option invalide pour l'adresse IPv4.")
    else:
        print("Base non reconnue.")

if __name__ == "__main__":
    main()
