from Domain.cheltuiala import *
from Logic.CRUD import *
from Logic.functionalitati import *


lista_default = [
    creeaza_cheltuiala(22, 145, "25.06.2021", "alte cheltuieli", 1),
    creeaza_cheltuiala(12, 348, "25.06.2021", "canal", 2),
    creeaza_cheltuiala(22, 165, "20.01.2019", "întreținere", 3),
    creeaza_cheltuiala(22, 200, "13.12.2018", "întreținere", 4),
]


def test_undo_redo():
    lista = []
    liste_undo = []
    liste_redo = []
    lista = adaugare_cheltuiala(lista_default[0], lista, liste_undo, liste_redo)
    lista = adaugare_cheltuiala(lista_default[1], lista, liste_undo, liste_redo)
    lista = adaugare_cheltuiala(lista_default[2], lista, liste_undo, liste_redo)
    assert len(liste_undo) == 3
    lista = undo(lista, liste_undo, liste_redo)
    assert len(lista) == 2
    assert liste_redo == 1
    lista = undo(lista, liste_undo, liste_redo)
    lista = undo(lista, liste_undo, liste_redo)
    lista = undo(lista, liste_undo, liste_redo)
    assert len(lista) == 0
    assert len(liste_undo) == 0
    assert len(liste_redo) == 3
    lista = adaugare_cheltuiala(lista_default[0], lista, liste_undo, liste_redo)
    lista = adaugare_cheltuiala(lista_default[1], lista, liste_undo, liste_redo)
    lista = adaugare_cheltuiala(lista_default[2], lista, liste_undo, liste_redo)
    lista = redo(lista, liste_undo, liste_redo)
    assert lista == lista_default[:3]
    lista = undo(lista, liste_undo, liste_redo)
    lista = undo(lista, liste_undo, liste_redo)
    lista = redo(lista, liste_undo, liste_redo)
    assert lista == lista[:2]
    lista = undo(lista, liste_undo, liste_redo)
    lista = undo(lista, liste_undo, liste_redo)
    assert lista == []
    lista = redo(lista, liste_undo, liste_redo)
    lista = adaugare_cheltuiala(lista_default[3], lista, liste_undo, liste_redo)
    lista = redo(lista, liste_undo, liste_redo)
    assert len(lista) == 2
    lista = redo(lista, liste_undo, liste_redo)
    assert len(lista) == 2
    assert lista == [lista_default[0], lista_default[3]]
    stergere_cheltuieli(22, lista, liste_undo, liste_redo)
    assert lista == []
    undo(lista, liste_undo, liste_redo)
    assert len(lista) == 2
    redo(lista, liste_undo, liste_redo)
    assert lista == []
