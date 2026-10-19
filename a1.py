#activitat 1
print("Hola món!")
#activitat 2
nombre1 = int(input("Introdueix el primer nombre: "))
nombre2 = int(input("Introdueix el segon nombre: "))
suma = nombre1 + nombre2
print("El resultat de la suma és:", suma)
#Activitat 3
a = 7
s = a % 2
print(s)
if s == 0:
    print(a, " es parell ")
else:
    print(a, " es senar ")
#Activitat 4
celsius = 25
Fahrenheit = (celsius * 9/5) + 32
print("La temperatura en Fahrenheit és:", Fahrenheit)
#Activitat 5
altura = 4
amplada = 5
area = altura * amplada
print("L'àrea del rectangle és:", area)
#Activitat 6
nombre = 6
for i in range(1, 11):
    print(nombre, "x", i, "=", nombre * i)
#Activitat 7
s= "Programació"
cont = 0
for c in s:
    print(c)
    cont+=1 #cont = cont +1

print("Nombre de lletres ", cont, "o amb len =", len(s))
for i in range(0, len(s)):
    print(s[i])
#Activitat 8
nombre = 8 
