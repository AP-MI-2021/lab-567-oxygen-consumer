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
