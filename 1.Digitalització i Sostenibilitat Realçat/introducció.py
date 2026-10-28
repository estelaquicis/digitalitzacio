print("Hello World!!")
a=1
print(a)
print(type(a))

b=False 
print(type(b))

if a==1: 
    print("estic dins")
else: #else sirve como un sino,e s decir otra opción 
    print("No és 1")

print("Fora del IF")

#FOR i RANGE (5 octubre)
for i in range ( 1,11):
print(“7 *” , i ,”=”,(i*7))

for i in range ( 1,11):
producte= i*7
print(“7 *” , i ,”=”,producte)

s = “hola
for c in s:
print(c)

for i in range(0,len(s)):
print(s[i])

cont = 0
for c in s:
    print(c)
    cont+=1 #cont = cont +1

print("Nombre de lletres ", cont, "o amb len =", len(s))

for i in range(0, len(s)):
    print(s[i])