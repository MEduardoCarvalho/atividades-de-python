pilha = []
num = str(input("digite a expressao"))
for c in num:
    if c == "(":
      pilha.append("(")
    elif c == ")":
      if len(pilha) > 0:
        pilha.pop()
      else:
        pilha.append(")")  
        break
if len(pilha) == 0:
  print("esta expressao esta certa")   
else:
  print("esta expressao esta errada")