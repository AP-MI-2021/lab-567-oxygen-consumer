from Domain.cheltuiala import get_nr_aparament


def stergere_cheltuieli(nr_apartament, lista):
    lista_noua = []
    for cheltuiala in lista:
        if get_nr_aparament(cheltuiala) != nr_apartament:
            lista_noua.append(cheltuiala)
    return lista_noua
