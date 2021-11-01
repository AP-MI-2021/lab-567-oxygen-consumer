from datetime import date, datetime


tipuri_permise = ["întreținere", "canal", "alte cheltuieli"]


def creeaza_cheltuiala(nr_apartament: int, suma: float, data: str, tip: str, id):
    """
    Returneaza un dictionar ce defineste o cheltuiala.

    Parametri:
    - nr_apartament: mumarul apartamentului
    - suma: suma cheltuielii
    - data: data in care s-a inregistrat cheltuiala
    - tip: tipul cheltuielii (întreținere, canal sau alte cheltuieli)
    - id: id-ul cheltuielii
    """

    if tip not in tipuri_permise:
        raise ValueError(f"tipurile permise sunt: {tipuri_permise}")

    if isinstance(data, str):
        data = str_to_date(data)

    return [
        nr_apartament,
        suma,
        data,
        tip,
        id,
    ]


def get_nr_aparament(cheltuiala):
    return cheltuiala[0]


def get_suma(cheltuiala):
    return cheltuiala[1]


def get_data(cheltuiala):
    return cheltuiala[2]


def get_tip(cheltuiala):
    return cheltuiala[3]


def get_id(cheltuiala):
    return cheltuiala[4]


def to_string(cheltuiala):
    return f"id: {get_id(cheltuiala)}, suma: {get_suma(cheltuiala)}, data: {get_data(cheltuiala).strftime('%d.%m.%Y')}, tip: {get_tip(cheltuiala)}"


def str_to_date(data):
    try:
        return datetime.strptime(data, "%d.%m.%Y").date()
    except:
        raise ValueError(
            "data trebuie sa fie valida si sa aiba urmatorul format: DD.MM.YYYY"
        )
