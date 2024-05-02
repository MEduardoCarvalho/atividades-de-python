fim = int(input("digite ate que termo voce quer ve:"))
c = 0
t1 = 0
t2 = 1
while c < fim:
  if c == 0:
    print(f"{t1} → ", end = "")
  elif c == 1:
    print(f"{t2} → ", end = "")
  else:
    t3 = t2 + t1
    print(f"{t3} → ", end = "")
    t1 = t2
    t2 = t3
  c +=1    
print("fim")
