from Logic.functionalitati import *
from Logic.CRUD import get_by_id
from Domain.cheltuiala import *


lista_default = [
    creeaza_cheltuiala(22, 145, "25.06.2021", "alte cheltuieli", 1),
    creeaza_cheltuiala(12, 348, "25.06.2021", "canal", 2),
    creeaza_cheltuiala(22, 165, "20.01.2019", "întreținere", 3),
    creeaza_cheltuiala(22, 200, "13.12.2018", "întreținere", 4),
]


def test_stergere_cheltuieli():
    lista = lista_default
    lista = stergere_cheltuieli(22, lista, [], [])
    assert len(lista) == 1
    assert get_by_id(1, lista) is None
    assert get_by_id(3, lista) is None
    assert get_by_id(4, lista) is None

    lista = lista_default
    lista = stergere_cheltuieli(13, lista, [], [])
    assert len(lista) == 4

    lista = stergere_cheltuieli(12, lista, [], [])
    assert len(lista) == 3
    assert get_by_id(2, lista) is None


def test_adauga_valoare_la_cheltuieli():
    lista = lista_default
    lista = adauga_valoare_la_cheltuieli("25.06.2021", 10, lista, [], [])
    assert len(lista) == 4
    assert get_suma(lista[0]) == 155
    assert get_suma(lista[1]) == 358
    assert get_suma(lista[2]) == 165
    assert get_suma(lista[3]) == 200


def test_cea_mai_mare_cheltuiala():
    lista = lista_default
    assert cea_mai_mare_cheltuiala("canal", lista) == lista[1]
    assert cea_mai_mare_cheltuiala("întreținere", lista) == lista[3]
    assert cea_mai_mare_cheltuiala("emacs > vim", lista) is None


def test_ordonare_descrescatoare():
    lista = lista_default
    lista = ordonare_descrescatoare(lista, [], [])
    assert len(lista) == 4
    assert get_suma(lista[0]) == 348
    assert get_suma(lista[-1]) == 145


def test_sume_lunare():
    lista = lista_default
    lista.append(creeaza_cheltuiala(22, 145, "03.06.2021", "canal", 5))
    sume = sume_lunare(lista)
    assert len(sume) == 3
    assert len(sume["06 2021"]) == 2
    assert sume["06 2021"][22] == 290


def test_functionalitati():
    test_stergere_cheltuieli()
    test_adauga_valoare_la_cheltuieli()
    test_cea_mai_mare_cheltuiala()
    test_ordonare_descrescatoare()
    test_sume_lunare()
