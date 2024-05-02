num = (int(input("digite um numero")),
       int(input("digite outro numero")),
       int(input("digite mais um numero")),
       int(input("digite o ultimo numero")))

if num.count(9) > 0:
  print(f"o numero 9 aparece{num.count(9)} vezes")
else:
  print("o numero 9 nao aparece")
if num.count(3) > 0:
  print(f"o numero 3 se encontra pela primeira vez na {num.index(3)+1} posiçao")
else:
  print("o numero 3 nao se encotra")
print("os numeros pares sao:", end= "")
for c in num:
  if c % 2 == 0:
    print(c , end = " ")
