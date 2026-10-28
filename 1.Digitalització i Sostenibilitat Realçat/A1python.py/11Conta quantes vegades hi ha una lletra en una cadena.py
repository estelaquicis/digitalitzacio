textdna =  "atggatcattta"
contador = 0

for letra in textdna:
    if letra == "a":
        contador += 1
        print("Posición:", contador)
print("Total:", textdna.count("a"))        