def modificar(lista):
    # Copia profunda de la lista para no modificar la original
    lista_modificada = lista.copy()
    
    # Eliminar elementos duplicados
    lista_modificada = list(set(lista_modificada))
    
    # Ordenar la lista de mayor a menor
    lista_modificada.sort(reverse=True)
    
    # Eliminar números impares
    lista_modificada = [num for num in lista_modificada if num % 2 == 0]
    
    # Realizar la suma de los números restantes
    suma = sum(lista_modificada)
    
    # Añadir la suma como primer elemento de la lista
    lista_modificada.insert(0, suma)
    
    return lista_modificada

# Ejemplo de uso
lista = [3, 7, 2, 3, 8, 2, 10]
nueva_lista = modificar(lista)
print(nueva_lista)
print(nueva_lista[0] == sum(nueva_lista[1:]))
