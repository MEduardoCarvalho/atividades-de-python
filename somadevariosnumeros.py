cont = soma = 0
while True:
  num = int(input("digite um numero [999 para parar]"))
  if num < 999:
    soma += num 
    cont +=1
  elif num == 999:
    break
  else:
    print("apenas suporto numeros abaixo de 999")
    print("tente denovo:")
print(f"foram digitado {cont} numeros e a soma de todoa é {soma}")     
