lista = []
op = "S"
while op == "S":
  lista.append(int("digite um numero"))
  op = ""
  while op != "S" :
    op = str(input("quer continuar [S|N]")).strip().upper()[0]
    if op == "N":
      break
print(f"foram resgistrado {len(lista)} numeros na lista")
lista.sort(reverse = True)
print(f"a lista em ordem decrecente {lista}")
if 5 in lista:
  print("o numero 5 esta na lista")
else:
  print("o numero 5 nao se encontra na lista")
