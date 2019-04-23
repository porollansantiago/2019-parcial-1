import math
#funcion que recibe un numero decimal y devuelve su equivalente en hexadecimal
def decimal_to_hex(decimal):
    hexadecimal = ''
    while True:
        if (decimal//16)//16 == 0:
            mod = decimal%16
            decimal = decimal//16
            if decimal != 0:
                hexadecimal = mod_to_hex(decimal) + mod_to_hex(mod)+ hexadecimal 
            elif decimal == 0:
                hexadecimal =  mod_to_hex(mod) + hexadecimal
            break
        mod = decimal%16
        decimal = decimal//16
        hexadecimal =mod_to_hex(mod)+ hexadecimal 
    return hexadecimal

def mod_to_hex(mod):
    if mod == 10:
        return 'A'
    elif mod == 11:
        return 'B'
    elif mod == 12:
        return 'C'
    elif mod == 13:
        return 'D'
    elif mod == 14:
        return 'E'
    elif mod == 15:
        return 'F'
    else:
        return str(mod)
    
