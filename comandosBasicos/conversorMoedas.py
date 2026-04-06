print("|", "=" * 50, "|")
print("\tSistema de conversão de moedas locais")
print("|", "=" * 50, "|")

continua = True

while continua:

  print("Escolha a moeda que vai ser convertida: ")
  moedaO = int(input("[1] - Real\n[2] - Dólar\n[3] - Euro\n"))


  valorO = float(input("Digite o valor: "))

  print("Escolha a moeda de conversão: ")

  match moedaO:
    case 1:
      moedaC = int(input("[1] - Dólar\n[2] - Euro\n"))

      match moedaC:
        case 1:
          valorC = valorO * 0.19
          print(f"O valor convertido é {valorC:.2F} dólares")
        case 2:
          valorC = valorO * 0.17
          print(f"O valor convertido é {valorC:.2f} euros")

    case 2:
      moedaC = int(input("[1] - Real\n[2] - Euro\n"))

      match moedaC:
        case 1:
          valorC = valorO * 5.15
          print(f"O valor convertido é {valorC:.2f} reais")
        case 2:
          valorC = valorO * 0.87
          print(f"O valor convertido é {valorC:.2f} euros")

    case 3:
      moedaC = int(input("[1] - Real\n[2] - Dolar\n"))

      match moedaC:
        case 1:
          valorC = valorO * 5.96
          print(f"O valor convertido é {valorC:.2f} reais")
        case 2:
          valorC = valorO * 1.16
          print(f"O valor convertido é {valorC:.2f} euros")


  contOp = int(input("Deseja continuar? [1] - sim [2] - não\n"))

  if contOp == 2:
    continua = False


