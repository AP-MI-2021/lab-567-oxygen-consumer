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
