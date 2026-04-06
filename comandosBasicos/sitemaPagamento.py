qtd  = int(input("Quantos produtos deseja adicionar? "))

while qtd <= 0:
  qtd  = int(input("Digite um valor válido: "))

total = 0

for i in range(1, qtd + 1):
  valor = float(input(f"Digite o valor do {i} produto: "))

  while valor <= 0:
    valor = float(input("Digite um valor válido: "))

  total += valor

print(f"\nTotal da compra: R${total:.2f}")

desconto = 0

if total > 100:
  desconto = total * 0.1
  total -= desconto
  print(f"Desconto para o valor da compra de R${desconto:.2f}")
else:
  print("Nenhum desconto aplicado.")

print("\nForma de pagamento: [1] À vista [2] Parcelado \n")
formaP = int(input())

while formaP != 1 and formaP != 2:
  formaP= int(input("Digite uma foma de pagamento válida!!!\n[1] - À vista [2] - Parcelado \n"))

if formaP == 1:
  desco_pag = total * 0.15
  total -= desco_pag
  print(f"Desconto de 15% aplicado: R${desco_pag:.2f}")
elif formaP == 2:
  parcelas = int(input("Pagamento parcelado"))
else:
  print("Opção inválida")

print(f"Valor final da compra: R${total:.2f}")
