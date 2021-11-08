from Domain.cheltuiala import *
from Logic.CRUD import *
from datetime import date


def stergere_cheltuieli(nr_apartament, lista, liste_undo, liste_redo):
    """
    Sterge toate cheltuielile asociate unui apartament din lista.
    """
    modificat = False
    liste_undo.append(lista)
    for cheltuiala in lista:
        if get_nr_aparament(cheltuiala) == nr_apartament:
            lista = stergere_cheltuiala(get_id(cheltuiala), lista, [], [])
            modificat = True
    if modificat:
        liste_redo.clear()
    else:
        liste_undo.pop()
    return lista


def adauga_valoare_la_cheltuieli(data, suma, lista, liste_undo, liste_redo):
    """
    Adauga o valoare la toate cheltuielile dintr-o anumita data.
    """
    data = str_to_date(data)
    modificat = False
    liste_undo.append(lista)
    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            modificat = True
            lista = modificare_cheltuiala(
                get_id(cheltuiala),
                get_nr_aparament(cheltuiala),
                get_suma(cheltuiala) + suma,
                get_data(cheltuiala),
                get_tip(cheltuiala),
                lista,
                [],
                [],
            )
    if modificat:
        liste_redo.clear()
    else:
        liste_undo.pop()
    return lista


def cea_mai_mare_cheltuiala(tip, lista):
    """
    Determina cheltuiala cu suma cea mai mare de un anumit tip din lista.
    """

    cheltuiala_max = None

    for cheltuiala in lista:
        if get_tip(cheltuiala) == tip and (
            cheltuiala_max is None or get_suma(cheltuiala) > get_suma(cheltuiala_max)
        ):
            cheltuiala_max = cheltuiala

    return cheltuiala_max


def ordonare_descrescatoare(lista, liste_undo, liste_redo):
    """
    Ordoneaza cheltuielile in ordine descrescatoare dupa suma.
    """
    liste_undo.append(lista)
    liste_redo.clear()
    lista.sort(reverse=True, key=lambda cheltuiala: get_suma(cheltuiala))
    return lista


def sume_lunare(lista):
    """
    Returneaza un dictionar de dictionare cu sumele lunare per apartament.
    """
    sume = {}
    for cheltuiala in lista:
        luna = get_data(cheltuiala).strftime("%m %Y")
        apartament = get_nr_aparament(cheltuiala)

        if luna not in sume:
            sume[luna] = {}

        if apartament in sume[luna]:
            sume[luna][apartament] += get_suma(cheltuiala)
        else:
            sume[luna][apartament] = get_suma(cheltuiala)

    return sume
