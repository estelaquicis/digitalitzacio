# Inverteix l’ordre dels elements d’una llista sense usar reverse().
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

llista_invertida = []

for x in range(len(list_num)):
    llista_invertida.append(list_num[len(list_num)-1-x])

print(llista_invertida)