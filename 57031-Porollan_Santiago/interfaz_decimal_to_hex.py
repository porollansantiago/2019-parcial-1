from decimal_to_hex import decimal_to_hex
#interfaz que se encarga de asegurarse que el valor que se pasa a la funcion es de tipo int
def interfaz_decimal_to_hex(word):
    try:
        word = int(word)
        return decimal_to_hex(word)
    except ValueError:
        return "Disculpe, solo acepto numeros"