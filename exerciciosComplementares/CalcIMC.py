# Calculo de IMC

continuacao = True
while (continuacao):
  
  print("******* Calculo de IMC *******")

  # determinação de sexo
  sexo = 0
  while sexo != 1 and sexo != 2:
    sexo = int(input("Digite seu sexo: \n[1] - Feminino \n[2] - Masculino\n"))
    if sexo != 1 and sexo != 2:
      print("Digite uma opção válida!")

  #Determinação de altura
  altura = float(input("Digite sua altura (m): "))
  if(altura < 0.9):
    print("Sai daqui gnomo!")
    break
  elif(altura > 2.5):
    print("Sai daqui poste!")
    break

  #Determinação de peso
  peso = float(input("Digite seu peso (kg): "))

  imc = peso /(altura **2)

  print("Seu IMC é ", imc)

  if sexo == 1:
    if ((imc > 30)):
      print("Você está acima do peso!")
    elif (imc > 25):
      print("Você está com sobrepeso!")
    elif (imc > 18.5):
      print("Você está no seu peso ideal!")
    elif(imc > 16):
      print("Você está abaixo do peso!")
    else:
      print("Olá varinha de condão!!")
  else:
    if ((imc > 30)):
      print("Você está acima do peso!")
    elif (imc > 25):
      print("Você está com sobrepeso!")
    elif (imc > 18.5):
      print("Você está no seu peso ideal!")
    elif(imc > 16):
      print("Você está abaixo do peso!")
    else:
      print("Olá espuleta!!")

  #Teste de continuidade
  continuacao = input("Deseja continuar? [S/N]")
  if continuacao == "S":
    continuacao = True
  elif continuacao == "N":
    continuacao = False
  else:
    print("Opção inválida, encerrando programa!")
    continuacao = False