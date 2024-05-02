num = 0
op = "S"
lista = []
while op == "S":
  num = int(input("digite um numero"))
  if num not in lista:
    lista.append(num)
    print("valor adicionado com sucesso")
  else:
    print("erro... nao adicionei pois o numero é duplicado")
  op = ""
  while op != "S":
    op = str(input("quer continuar [S|N]")).strip().upper()[0]
    if op == "N":
      break
lista.sort()
for c in lista:
  print(c, end = "-")
