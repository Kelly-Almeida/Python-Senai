time = input("Entre com o nome de um time de futebol: ")

match time:
  case "Flamengo" | "Bahia" | "Vitória" | "Nenhum": #Separação de strings
    print("Excelente escolha!!")
  case "Palmeiras":
    print("Time de indiano vagabundo!!")
  case "Corinthias" | "São Paulo":
    print("Time de paulistinha")
  case "Botafogo":
    print("Andrei é vc, demônio?")
  case _: #Outro caso
    print("Oh demônio!")
