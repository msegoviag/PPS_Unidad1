# Traductor binario a decimal.
def esBinario(strbinario):
    try:
        return int(strbinario,2)
    except (ValueError, TypeError) as error:
        return "El numero introducido no es decimal"
        
numeroBinario = input("Introduce el numero en binario: ")
print(esBinario(numeroBinario))
   
