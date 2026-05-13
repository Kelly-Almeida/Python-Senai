nome = input("Digite seu nome: ");
livro = input("Nome do livro: ");
quantPaginas = int(input("Quantidade de páginas do livro: "));
temp = int(input("Tempo médio de leitura por página em segundos: "));

tempTotal = (quantPaginas * temp)/360;
print(f"{nome} você finalizará a leitura do livro {livro} em aproximadamente {tempTotal:.2f} horas")