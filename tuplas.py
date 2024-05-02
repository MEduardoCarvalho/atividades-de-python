produto = ("abacate", 10.2, 
           "banana", 9,
           "pera", 8.40,
           "uva", 5,
           "pessego",9.25,
           "morango",2.30,
           "manga", 5.59,
           "melancia", 3.99,
           "amendoin", 1.23,
           "couve" , 4.50 )      
print("=" * 27)
print(f'{"LISTAGEM DE PREÇOS":^27}')
print("=" * 27)
for c in range(0,len(produto)):
  if c % 2 == 0:
    print(f" {produto[c]:.<15}", end = "")
  else:
    print(f"R${produto[c]:>7.2f}")
