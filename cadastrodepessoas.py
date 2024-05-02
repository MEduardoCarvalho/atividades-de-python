cont = homens = mulher = 0
while True:
  print("--" * 15)
  print("     cadastre uma pessoa")
  print("--" * 15)
  idade = int(input("idade "))
  sexo = " "
  while sexo not in "F" and sexo not in "M":
    sexo = str(input("sexo [M|F]")).strip().upper()[0]
  if idade >= 18:
    cont += 1
  if sexo in "M":
     homens+= 1
  if sexo in "F" and idade < 20:
    mulher +=1
  opçao = " "
  while opçao not in "S" and opçao not in "N":
    opçao =str(input("quer continua [S|N]")).strip().upper()
  if opçao in "N":
      break
print("====== FIM DO PROGRAMA ======")    
print(f"todas as pessoas com menos de 18: {cont}") 
print(f"ao todo temos {homens} homens cadastrados")
print(f"e temos {mulher} mulheres menores de 20 anos")
