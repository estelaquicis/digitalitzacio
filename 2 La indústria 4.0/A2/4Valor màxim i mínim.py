# Troba el valor més gran i el més petit dins d’una llista.
# Troba el valor més gran i el més petit dins d’una llista.
list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]

maxim = None
minim = None

for num in list_num:
    if maxim == None or num > maxim:
        maxim = num


    if minim == None or num < minim:
        minim = num


print("Valor màxim:", maxim)
print("Valor mínim:", minim)
