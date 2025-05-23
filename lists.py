# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    lista = list_to_remove_elements
    if len(lista) < 2:
        return[]
    elif len(lista) >= 2 and len(lista) < 5:
        return lista[1:]
    elif len(lista) == 5 or len(lista) == 6:
        return lista[1:4]
    else:
        return lista[1:4] + lista[6:0]

def add_elements(list_to_add_elements):
    lista = list_to_add_elements
    lista.insert(0, "Pink")
    lista.append("Yellow")
    return lista

def is_empty(list_to_check):
    lista = list_to_check
    if len(lista) == 0:
        return "Lista vacia"

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) < 3 or len(list_to_compare2) < 3:
        return False
    elif list_to_compare1[2] == list_to_compare2[2]:
        return True
    else:
        return False    

def list_of_lists(list_of_lists_to_modify):
    lista = list_of_lists_to_modify
    listamodificada = [lista[0][0:2],lista[1][1:4],lista[2][-2:]]
    return listamodificada    
