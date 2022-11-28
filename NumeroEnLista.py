
# Se comprueba si el número está en la lista.
def estaEnLista(num, lista):

    if num in lista:
        print("El número está dentro de la lista.")
    else:
        print("El número no está dentro de la lista.")

# Se comprueba si el número está dentro del rango, si lo está entonces se chequea si está dentro de la lista.


def estaEnRango(valor, minimo, maximo):

    if valor < minimo or valor > maximo:
        print("El número está fuera del rango de la lista")
        return
    else:
        print("El número esta dentro del rango de la lista")

# Ejecución segura ante fallos, solo se permitirá numeros no letras.


try:
    lista = [6, 14, 11, 3, 2, 1, 15, 19]
    estaEnRango(3, 5, 10)
    estaEnLista(3, lista)
except (ValueError, TypeError):
    print("Introduce únicamente números")
