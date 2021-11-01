from Domain.cheltuiala import *
from datetime import date


def test_cheltuiala():
    cheltuiala = creeaza_cheltuiala(40, 230, "25.04.2021", "canal", 9)

    assert get_nr_aparament(cheltuiala) == 40
    assert get_suma(cheltuiala) == 230
    assert get_data(cheltuiala) == date(2021, 4, 25)
    assert get_tip(cheltuiala) == "canal"
    assert get_id(cheltuiala) == 9
