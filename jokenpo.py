from random import randint
from time import sleep

print("jogue jokenpo comigo")
print("boa sorte!!!")
computer = randint(1,3)
print("1 - pedra")
print("2 - papel")
print("3 - tesoura")
usuario = int(input("qual sua jogado:"))
if usuario <= 3 and usuario > 0:
 print("JO")
 sleep(1)
 print("KEN")
 sleep(1)
 print("PO!!!")
 print("-=" * 13)
if computer == 1 and usuario == 2:
  print("sua jogada foi Papel")
  print("computador jogou pedra")
  print("-=" * 13)
  print("parabens voce ganhou")
elif computer == 1 and usuario == 3:
  print("sua jogada foi tesoura")
  print("computador jogou pedra")
  print("-=" * 13)
  print("voce perdeu")
elif computer == 2 and usuario == 1:
  ptint("sua jogada foi pedra")
  print("computar jogou papel")
  print("-=" * 13)
  print("voce perdeu")
elif computer == 2 and usuario == 3:
  print("sua jogada foi tesoura")
  print("computador jogou papel")
  print("-=" * 13)
  print("parabens voce ganhou")
elif computer == 3 and usuario == 2:
  print("sua jogada foi papel")
  print("computador jogou tesoura")
  print("-=" * 13)
  print("voce perdeu")
elif computer == 3 and usuario ==1:
  print("sua jogada foi pedra")
  print("computador jogou tesoura")
  print("-=" * 13)
  print("parabens voce ganhou")
elif computer == usuario:
  print("usuario e computador")
  print("fizeram a mesma jogada")
  print("-=" * 13)
  print("empate")
else:
  print("digite um numero certo!!")
