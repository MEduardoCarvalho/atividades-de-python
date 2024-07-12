termo = int(input("digite o primeiro termo "))
razao = int(input("digitea razao "))
c=0
fim = 10
print(f"{termo} ", end = "")
while c < fim:
  termo += razao
  print(f"{termo} " , end = "")
  c+=1
  if c == fim:
    num = int(input(" \n quer mais quantos termos "))
    fim += num
print(f"foram mostrado {fim} termos")


