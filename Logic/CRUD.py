from Domain.cheltuiala import creeaza_cheltuiala, get_id


def adaugare_cheltuiala(cheltuiala, lista):
    """
    Adauga o cheltuiala la lista de cheltuieli si returneaza noua lista.
    """
    return lista + [cheltuiala]


def stergere_cheltuiala(id, lista):
    """
    Sterge o cheltuiala din lista de cheltuieli si returneaza noua lista.
    """
    return [cheltuiala for cheltuiala in lista if get_id(cheltuiala) != id]


def modificare_cheltuiala(id, nr_apartament, suma, data, tip, lista):
    """
    Inlocuieste o cheltuiala cu una noua in lista de cheltuieli si returneaza
    noua lista.
    """
    lista_noua = []
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
