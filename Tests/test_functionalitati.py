from Logic.functionalitati import *
from Logic.CRUD import get_by_id
from Domain.cheltuiala import *


lista_default = [
    creeaza_cheltuiala(22, 145, "25.06.2021", "alte_cheltuieli", 1),
    creeaza_cheltuiala(12, 348, "25.06.2021", "canal", 2),
    creeaza_cheltuiala(22, 165, "20.01.2019", "întreținere", 3),
]


def test_stergere_cheltuieli():
    lista = lista_default
    lista = stergere_cheltuieli(22, lista)
    assert len(lista) == 1
    assert get_by_id(1, lista) is None
    assert get_by_id(3, lista) is None

    lista = lista_default
    lista = stergere_cheltuieli(13, lista)
    assert len(lista) == 3

    lista = stergere_cheltuieli(12, lista)
    assert len(lista) == 2
    assert get_by_id(2, lista) is None


def test_adauga_valoare_la_cheltuieli():
    lista = lista_default
    lista = adauga_valoare_la_cheltuieli("25.06.2021", 10, lista)
    assert len(lista) == 3
    assert get_suma(lista[0]) == 155
    assert get_suma(lista[1]) == 358
    assert get_suma(lista[2]) == 165


def test_functionalitati():
    test_stergere_cheltuieli()
    test_adauga_valoare_la_cheltuieli()
