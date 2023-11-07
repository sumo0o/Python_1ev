#haz un programa que lea un número y sume todas sus cifras

num = str(input("Ingrese un número: "))
suma = 0

for i in range (0, int(len(num))):
  suma += int(str(num)[i])
  
print(suma)
