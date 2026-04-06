valor = 0

print("==================================\n")
print("\tCRIANÇA ESPERANÇA\n")
print("==================================\n")

print("Muito obrigada pela ajuda!!\n")
print("Digite...\n")
print("[1] - Para doar R$10,00\n")
print("[2] - Para doar R$20,00\n")
print("[3] - Para doar R$50,00\n")
print("[4] - Para doar R$100,00\n")
print("[5] - Para outros valores\n")

op = int(input())

match op:
  case 1: valor = 10
  case 2: valor = 20
  case 3: valor = 50
  case 4: valor = 100
  case 5:
    valor = float(input("Digite o valor que deseja doar: "))


print("==================================\n")
print(f"\tSua doação foi de \n\t    R${valor:.2f}\n")
print("\tMuito Obrigado!!")
print("==================================\n")
