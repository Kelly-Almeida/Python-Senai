valor = float(input("Digite o valor da mercadoria: "))
formaP = int(input("Metodo de pagamento: \n[1] - Pix\n[2] - Cartão\n"))

match formaP:
  case 1:
    valorPix = valor * 0.9
    print(f"O valor com desconto pix é de {valorPix:.2f}")
    print("Código pix sendo gerado...")

  case 2:
    formaC = int(input("Digite a forma de pagamento: \n[1] - Debito\n[2] - Crédito\n"))
    match formaC:
      case 1:
        print("Aproxime ou insira o cartão...")
      case 2:
        if valor > 1000:
          parcelas = valor /5
          print(f"Você pode parcelar o valor em 5x de R$: {parcelas:.2f}")
        else:
          parcelas = valor/ 3
          print(f"Você pode parcelar o valor em 3x de R$: {parcelas:.2f}")
      case _:
        print("Opção inválida!! Pagamento cancelado!")
  case _:
   print("Opção inválida!! Pagamento cancelado!")
