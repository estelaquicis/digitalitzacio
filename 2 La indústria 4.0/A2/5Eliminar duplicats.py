# Donada una llista amb elements repetits, crea una nova llista sense duplicats.

llist_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
lista_nova = []
for x in llist_num:
    esta = False

    for y in lista_nova:
        if x == y:
            esta = True

    if esta == False:
        lista_nova.append(x)
print(lista_nova)
