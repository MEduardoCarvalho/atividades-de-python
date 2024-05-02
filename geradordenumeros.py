from random import randint

num = (randint(0,999),
       randint(0,999),
       randint(0,999),
       randint(0,999),
       randint(0,999))
print("numeros gerados foram ", end="")
for c in num:
  print(f"{c} ", end = "")
print(f"\no menor foi {sorted(num)[0]}")
print(f"o maior foi {sorted(num)[-1]}")
