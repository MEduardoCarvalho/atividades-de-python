c = maior = menor = total = 0

while True:
  c += 1
  print("======NOVO PRODUTO======")
  nome = str(input("nome:"))
  preço = int(input("valor:"))
  total += preço
  if c == 1:
    menor = preço
    barato = nome
  if preço < menor:
    menor = preço
    barato = nome
  if preço > 1000:
    maior +=1
  cont = str(input("quer continuar [S|N]")).strip().upper()[0]
  while cont not in "S" and cont not in "N":
      cont = str(input("quer continuar [S|N]")).strip().upper()[0]
  if cont == "N":
    break  
print(f"o tota da compra foi {total}")   
print(f" temos {maior} produtos custando mais que 1000 reais")
print(f"o mais barato foi {barato} e custou {menor:.2f} ")
