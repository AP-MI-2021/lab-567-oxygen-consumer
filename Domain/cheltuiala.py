from uuid import uuid4


def creeaza_cheltuiala(nr_apartament: int, suma: int, data: str, tip: str,
                       id = uuid4()):
    """
    Returneaza un dictionar ce defineste o cheltuiala.

    Parametri:
    - nr_apartament: mumarul apartamentului
    - suma: suma cheltuielii
    - data: data in care s-a inregistrat cheltuiala
    - tipul: tipul cheltuielii (întreținere, canal sau alte cheltuieli)
    """

    return {
        "nr_apartament": nr_apartament,
        "suma": suma,
        "data": data,
        "tip": tip,
        "id": id
    }


def get_nr_aparament(cheltuiala):
    return cheltuiala["nr_apartament"]


def get_suma(cheltuiala):
    return cheltuiala["suma"]


def get_data(cheltuiala):
    return cheltuiala["data"]


def get_tip(cheltuiala):
    return cheltuiala["tip"]

def get_id(cheltuiala):
    return cheltuiala["id"]
