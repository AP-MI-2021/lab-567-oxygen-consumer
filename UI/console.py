from Logic.CRUD import *
from Domain.cheltuiala import creeaza_cheltuiala, to_string
from Logic.functionalitati import *


def ui_adaugare_cheltuiala(lista):
    id = input("Introduceti id: ")

    try:
        nr_apartament = int(input("Introduceti nr apartamentului: "))
        suma = float(input("Introduceti suma: "))
        data = input("Intrdouceti data: ")
        tip = input("Introduceti tipul cheltuielii: ")
        lista = adaugare_cheltuiala(
            creeaza_cheltuiala(nr_apartament, suma, data, tip, id), lista
        )
    except ValueError as error:
        print(f"Eroare: {error}")

    return lista


def ui_stergere_cheltuiala(lista):
    id = input("Introduceti id-ul cheltuielii: ")
    lista = stergere_cheltuiala(id, lista)
    return lista


def ui_modificare_cheltuiala(lista):
    id = input("Introduceti id-ul cheltuielii: ")

    try:
        nr_apartament = int(input("Introduceti nr apartament: "))
        suma = float(input("Intoduceti suma: "))
        data = input("Introduceti data: ")
        tip = input("Introduceti tipul cheltuielii: ")

        lista = modificare_cheltuiala(id, nr_apartament, suma, data, tip, lista)
    except ValueError as error:
        print(f"Eroare: {error}")
    return lista


def ui_stergere_cheltuieli(lista):
    try:
        nr_apartament = int(input("Introduceti nr apartament: "))
        lista = stergere_cheltuieli(nr_apartament, lista)
    except ValueError as error:
        print(f"Eroare: {error}")
    return lista


def ui_adauga_valoare_la_cheltuieli(lista):
    try:
        data = input("Introduceti data: ")
        suma = float(input("Introduceti suma: "))
        lista = adauga_valoare_la_cheltuieli(data, suma, lista)
    except ValueError as error:
        print(f"Eroare: {error}")
    return lista


def print_usage():
    usage = """
a. Afisare lista cheltuieli
m. Afisare meniu
u. Undo
x. Iesire

1. Adaugare cheltuiala
2. Stergere cheltuiala
3. Modificare cheltuiala
4. Stergere toate cheltuielile pt un anumit apartament
5. Adunarea unei valori la toate cheltuielile dintr-o anumita data
    """
    print(usage)


def run_menu(lista):
    print_usage()
    liste_anterioare = []

    while True:
        optiune = input("Introduceti optiunea: ")

        if optiune == "x":
            break
        elif optiune == "a":
            # FIXME apare un None la capatul listei, nuj dc
            for cheltuiala in lista:
                print(to_string(cheltuiala))
        elif optiune == "m":
            print_usage()
        elif optiune == "u":
            try:
                lista = liste_anterioare[-1]
                liste_anterioare.pop()
            except IndexError:
                print("Eroare: nu mai puteti da undo")

        elif optiune == "1":
            liste_anterioare.append(lista)
            lista = ui_adaugare_cheltuiala(lista)
        elif optiune == "2":
            liste_anterioare.append(lista)
            lista = ui_stergere_cheltuiala(lista)
        elif optiune == "3":
            liste_anterioare.append(lista)
            lista = ui_modificare_cheltuiala(lista)
        elif optiune == "4":
            liste_anterioare.append(lista)
            lista = ui_stergere_cheltuieli(lista)
        elif optiune == "5":
            liste_anterioare.append(lista)
            lista = ui_adauga_valoare_la_cheltuieli(lista)

        else:
            print("Optiune inexistenta!")

    return lista
