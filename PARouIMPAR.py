import random

vitoria = 0
while True:
  print("Jogue PAR ou Impar")
  print("=-" * 18)
  num = int(input("diga um valor"))
  pi = " "
  while pi not in "PI":
    pi = str(input("Par ou Impar? [P|I]")).strip().upper()[0]
  print("=-" * 18)
  nu2 = random.randint(0,10)
  result = (nu2 + num) % 2
  print(f"voce jogou {num} e o computador jogou {nu2}")
  print(f"total de {num+nu2} deu " , end = "")
  if pi in "I":
    if result == 1:
        print("IMPAR \n" , "=-" * 18)
        print("voce ganhou parabens")
        vitoria += 1
    elif result == 0:
        print("PAR \n" , "=-" * 18)
        print("voce perdeu")
        break
  elif pi in "P":
    if result == 0:
        print("PAR \n" , "=-" * 18)
        print("parabens vc ganhou")
        vitoria += 1
    elif result == 1:
        print("IMPAR \n" , "=-" * 18)
        print("voce perdeu")
        break        
print(f"GAME OVER! voce teve a sequencia de {vitoria} vitorias")
