def place_dumpsters(L, k):
    dumpsters = []
    dump_count = 0
    street = L[-1]

    for house in L:
        if dump_count == 0:
            if house + k > street:
                p = street
            else:
                p = house + k
            dumpsters.append(p)
            dump_count += 1
        else:
            if house > dumpsters[-1] + k:
                if house + k > street:
                    p = street
                else:
                    p = house + k
                dumpsters.append(p)
                dump_count += 1
    return dumpsters


def select_a(lista):
    lista.sort(key = lambda x: x[1])
    libero = 0
    sol = []
    for inizio, fine in lista:
        if libero < inizio:
            sol.append((inizio, fine))
            libero = fine
    return sol