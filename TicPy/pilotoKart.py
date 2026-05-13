tamanhoPista = float(input("Tamanho da pista (m): "));
quantVoltas = int(input("Quantidade de voltas: "));
temp = float(input("Tempo estimado da primeira volta: "));

distanciaKm = (tamanhoPista/ 1000) * quantVoltas;
prevConclusao = (temp/60) * quantVoltas;

print(f"Análise Preditiva Concluída\n--\nDistância total a ser percorrida: {distanciaKm:.2f} km.\nPrevisão de conclusão {prevConclusao:.2f} minutos")
