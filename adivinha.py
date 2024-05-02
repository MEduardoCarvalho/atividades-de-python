import random

com = random.randint(0,10)
cont = 1
print("acabei de pensar em um nmero de 0 a 10 ")
num = int(input(" em qual numero estou pensando "))
while num != com:
  if num > com:
    num = int(input("menos... tente dnv:",))
  if num < com:
    num = int(input("mais... tente dnv:"))
  cont +=1
print(f" parabens voce conseguiu, depois de {cont} tentativa")  
