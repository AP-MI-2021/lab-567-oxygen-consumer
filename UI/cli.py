from Logic.CRUD import *
from Domain.cheltuiala import *


def run_add(params, lista):
    param_4 = params[4]
    try:
        param_4 = param_4 + " " + params[5]
    except:
        pass

    lista = adaugare_cheltuiala(
        creeaza_cheltuiala(
            int(params[1]), float(params[2]), params[3], param_4, params[0]
        ),
        lista,
    )
    return lista


def run_delete(id, lista):
    lista = stergere_cheltuiala(id, lista)
    return lista


def run_update(params, lista):
    param_4 = params[4]
    try:
        param_4 = param_4 + " " + params[5]
    except:
        pass

    lista = modificare_cheltuiala(
        params[0], int(params[1]), float(params[2]), params[3], param_4, lista
    )
    return lista


def show_all(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))


def print_usage():
    usage = """
Adaugare: add [id] [nr apartament] [suma] [data] [tip]
Stergere: delete [id]
Modificare: update [id] [nr apartament] [suma] [data] [tip]
Afisare: showall

Meniu: help
Iesire: exit
"""
    print(usage)


def run_cli(lista):
    print_usage()
    should_run = True

    while should_run:
        optiuni = input("$ ")
        optiuni = optiuni.split(";")

        try:
            for optiune in optiuni:
                optiune = optiune.split()

                if optiune[0] == "exit":
                    should_run = False
                    break
                elif optiune[0] == "help":
                    print_usage()
                elif optiune[0] == "showall":
                    show_all(lista)

                elif optiune[0] == "add":
                    lista = run_add(optiune[1:], lista)
                elif optiune[0] == "delete":
                    lista = run_delete(optiune[1], lista)
                elif optiune[0] == "update":
                    lista = run_update(optiune[1:], lista)

                else:
                    print("Optiune inexistenta")
        except Exception as error:
            print(f"Eroare: {error}")
