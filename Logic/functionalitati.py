from Domain.cheltuiala import *
from Logic.CRUD import *


def stergere_cheltuieli(nr_apartament, lista):
    """
    Sterge toate cheltuielile asociate unui apartament din lista.
    """
    for cheltuiala in lista:
        if get_nr_aparament(cheltuiala) == nr_apartament:
            lista = stergere_cheltuiala(get_id(cheltuiala), lista)
    return lista


def adauga_valoare_la_cheltuieli(data, suma, lista):
    """
    Adauga o valoare la toate cheltuielile dintr-o anumita data.
    """

    data = str_to_date(data)

    for cheltuiala in lista:
        if get_data(cheltuiala) == data:
            lista = modificare_cheltuiala(
                get_id(cheltuiala),
                get_nr_aparament(cheltuiala),
                get_suma(cheltuiala) + suma,
                get_data(cheltuiala),
                get_tip(cheltuiala),
                lista,
            )
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


def ordonare_descrescatoare(lista):
    """
    Ordoneaza cheltuielile in ordine descrescatoare dupa suma.
    """
    lista.sort(reverse=True, key=lambda cheltuiala: get_suma(cheltuiala))
    return lista
