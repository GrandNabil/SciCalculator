def conversion_bases(nombre_entree, base_entree=10):
    decimal = int(str(nombre_entree), base_entree)

    binaire = bin(decimal)[2:]  # [2:] pour enlever le préfixe
    octal = oct(decimal)[2:]
    hexadecimal = hex(decimal)[2:]

    return {
        "décimal": decimal,
        "binaire": binaire,
        "octal": octal,
        "hexadécimal": hexadecimal
    }