
# Se comprueba si el número está en la lista.
def estaEnLista(num, lista):

    if num in lista:
        print("El número " + str(num) + " está dentro de la lista.")
    else:
        print("El número  " + str(num) + "  no está dentro de la lista.")

# Se comprueba si el número está dentro del rango, si lo está entonces se chequea si está dentro de la lista.


def estaEnRango(valor, minimo, maximo):

    if valor < minimo or valor > maximo:
        print("El número " + str(valor) + " está fuera del rango de la lista")
        return
    else:
        print("El número " + str(valor) + " está dentro del rango de la lista")

# Ejecución segura ante fallos, solo se permitirá numeros no letras.


try:
    lista = [6, 14, 11, 3, 2, 1, 15, 19]
    estaEnRango(5, 5, 10)
    estaEnLista(-1, lista)
except (ValueError, TypeError):
    print("Introduce únicamente números")
