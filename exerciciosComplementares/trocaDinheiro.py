# Troca de dinheiro

#Funções
  #Quantidade de notas
def quantNotas(Din, Nota):
  if (Din/Nota) >= 1:

    if Nota > 1:
      print(Din//Nota, " nota(s) de ", Nota, " reais")

    elif Nota > 0:
      print(Din//Nota, " moeda(s) de ", (Nota * 100), " centavos")

    else:
      print(Din//Nota, " moedas(s) de ", Nota, " real")

    Din = Din % Nota


  return Din

  #Quantidade de moedas


#Entrada da quantidade de dinheiro
quantDin = float(input("Qual nota deseja trocar? "))
print("Em sua troca poderá ter:\n")

# Separação em notas
quantDin = quantNotas(quantDin, 100)
quantDin = quantNotas(quantDin, 50)
quantDin = quantNotas(quantDin, 20)
quantDin = quantNotas(quantDin, 10)
quantDin = quantNotas(quantDin, 5)
quantDin = quantNotas(quantDin, 2)

# Separação em moedas

quantDin = quantNotas(quantDin, 1)
quantDin = quantNotas(quantDin, 0.50)
quantDin = quantNotas(quantDin, 0.25)
quantDin = quantNotas(quantDin, 0.10)
quantDin = quantNotas(quantDin, 0.05)