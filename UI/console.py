from Logic.CRUD import *
from Domain.cheltuiala import creeaza_cheltuiala
from Logic.functionalitati import *


def ui_adaugare_cheltuiala(lista):
    id = input("Introduceti id: ")
    while get_by_id(id, lista) is not None:
        print("Id deja existent!")
        id = input("Introduceti id: ")

    nr_apartament = int(input("Introduceti nr apartamentului: "))
    suma = float(input("Introduceti suma: "))
    data = input("Intrdouceti data: ")
    tip = input("Introduceti tipul cheltuielii: ")

    lista = adaugare_cheltuiala(
        creeaza_cheltuiala(nr_apartament, suma, data, tip, id), lista
    )
    return lista


def ui_stergere_cheltuiala(lista):
    id = input("Introduceti id-ul cheltuielii: ")
    lista = stergere_cheltuiala(id, lista)
    return lista


def ui_modificare_cheltuiala(lista):
    id = input("Introduceti id-ul cheltuielii: ")
    if get_by_id(id, lista) is None:
        print("Id inexistent!")
        return lista

    nr_apartament = int(input("Introduceti nr apartament: "))
    suma = float(input("Intoduceti suma: "))
    data = input("Introduceti data: ")
    tip = input("Introduceti tipul cheltuielii: ")

    lista = modificare_cheltuiala(id, nr_apartament, suma, data, tip, lista)
    return lista


def ui_stergere_cheltuieli(lista):
    nr_apartament = int(input("Introduceti nr apartamentului: "))
    lista = stergere_cheltuieli(nr_apartament, lista)
    return lista


def print_usage():
    usage = """
a. Afisare lista cheltuieli
m. Afisare meniu
x. Iesire

1. Adaugare cheltuiala
2. Stergere cheltuiala
3. Modificare cheltuiala
4. Stergere toate cheltuielile pt un anumit apartament
    """
    print(usage)


def run_menu(lista):
    print_usage()

    while True:
        optiune = input("Introduceti optiunea: ")

        if optiune == "x":
            break
        elif optiune == "a":
            for cheltuiala in lista:
                print(cheltuiala)
        elif optiune == "m":
            print_usage()

        elif optiune == "1":
            lista = ui_adaugare_cheltuiala(lista)
        elif optiune == "2":
            lista = ui_stergere_cheltuiala(lista)
        elif optiune == "3":
            lista = ui_modificare_cheltuiala(lista)
        elif optiune == "4":
            lista = ui_stergere_cheltuieli(lista)

        else:
            print("Optiune inexistenta!")

    return lista
