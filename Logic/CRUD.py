from Domain.cheltuiala import creeaza_cheltuiala, get_id


def adaugare_cheltuiala(cheltuiala, lista, liste_undo, liste_redo):
    """
    Adauga o cheltuiala la lista de cheltuieli si returneaza noua lista.
    """
    if get_by_id(get_id(cheltuiala), lista) is not None:
        raise ValueError("Id-ul exista deja!")
    liste_undo.append(lista)
    liste_redo.clear()
    return lista + [cheltuiala]


def stergere_cheltuiala(id, lista, liste_undo, liste_redo):
    """
    Sterge o cheltuiala din lista de cheltuieli si returneaza noua lista.
    """
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat")
    liste_undo.append(lista)
    liste_redo.clear()
    return [cheltuiala for cheltuiala in lista if get_id(cheltuiala) != id]


def modificare_cheltuiala(
    id, nr_apartament, suma, data, tip, lista, liste_undo, liste_redo
):
    """
    Inlocuieste o cheltuiala cu una noua in lista de cheltuieli si returneaza
    noua lista.
    """
    lista_noua = []
    if get_by_id(id, lista) is None:
        raise ValueError("Nu exista o cheltuiala cu id-ul dat")
    liste_undo.append(lista)
    liste_redo.clear()
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            lista_noua.append(creeaza_cheltuiala(nr_apartament, suma, data, tip, id))
        else:
            lista_noua.append(cheltuiala)
    return lista_noua


def get_by_id(id, lista):
    """Returneaza cheltuiala cu id-ul specificat din lista."""
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None


def undo(lista, liste_undo, liste_redo):
    if len(liste_undo) == 0:
        return lista
    liste_redo.append(lista)
    lista = liste_undo.pop()
    return lista


def redo(lista, liste_undo, liste_redo):
    if len(liste_redo) == 0:
        return lista
    liste_undo.append(lista)
    lista = liste_redo.pop()
    return lista
