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
            



houses = [2,5,7,11,14,16,18]
k = 3
print(place_dumpsters(houses, k))