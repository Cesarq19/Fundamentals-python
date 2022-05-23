# Se hizo una funcion para filtrar una lista de numeros enteros positivos usando instance
def filter_list(l): 
    return list(filter(lambda x: isinstance(x,int),l))


