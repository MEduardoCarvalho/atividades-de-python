while True:
  print("-" * 33)
  num = int(input("quer ve a tabuada de qual numero "))
  print("-" * 33)
  c = 1
  if num < 0:
    print("Tabuada encerada. volte sempre!")
    break
  else:
      while c <= 10: 
        print(f" {num} x {c} = {c*num}") 
        c +=1
