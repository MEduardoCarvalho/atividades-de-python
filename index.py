print("==" * 15)
print("        BANCO DA NINA")
print("==" * 15)
while True:
    valor = int(input("qual valor deseja sacar R$:"))
    if valor >= 50:
      di50 = valor // 50
      print(f"total de {di50} cedulas de R$50")
      valor = valor - di50 * 50
    if valor >= 20:
      di20 = valor // 20
      print(f"total de {di20} cedulas de R$20")
      valor = valor - di20 * 20
    if valor >= 10:
      di10 = valor // 10
      print(f"total de {di10} cedulas de R$10")
      valor = valor - di10 * 10
    if valor >= 1:
      di1 = valor // 1
      print(f"total de {di1} cedulas de R$1")
      valor = valor - di1 * 1
    if valor == 0:
      break
    if valor < 0:
      print("ERRO!!! Digite novamente")
print("==" * 15)
print("volte sempree ao banco NINA! \n tenha um bom dia!")