from Logic.CRUD import *
from Domain.cheltuiala import *
from datetime import date


lista_default = [
    creeaza_cheltuiala(22, 145, "25.06.2021", "alte cheltuieli", 1),
    creeaza_cheltuiala(12, 348, "18.03.2020", "canal", 2),
]


def test_get_by_id():
    lista = lista_default
    assert get_by_id(1, lista) == lista[0]
    assert get_by_id(2, lista) == lista[1]
    assert get_by_id(3, lista) is None


def test_adaugare_cheltuiala():
    lista = []
    lista = adaugare_cheltuiala(lista_default[0], lista)
    assert len(lista) == 1
    assert get_suma(lista[0]) == 145
    assert get_data(lista[0]) == date(2021, 6, 25)
    assert get_tip(lista[0]) == "alte cheltuieli"
    assert get_id(lista[0]) == 1


def test_stergere_cheltuiala():
    lista = lista_default
    lista = stergere_cheltuiala(2, lista)
    assert len(lista) == 1
    assert get_by_id(1, lista) is not None
    assert get_by_id(2, lista) is None


def test_modificare_cheltuiala():
    lista = []
    lista = adaugare_cheltuiala(lista[0], lista)
    modificare_cheltuiala(1, 40, 120, "10.09.2018", "alte cheltuieli", lista)
    assert len(lista) == 1
    assert lista[0] == creeaza_cheltuiala(30, 120, "10.09.2018", "alte cheltuieli", 1)


def test_crud():
    test_get_by_id()
    test_adaugare_cheltuiala()
    test_stergere_cheltuiala()
