# PROGRAMA DE APRESENTAÇÃO SIMPLES
continuar = True;

nome = [];
curso = [];
periodo = [];
hobby = [];

while continuar:
    print("----------------------------------------------------\n");
    print("\tVamos fazer algumas breves apresentação\n");
    print("----------------------------------------------------\n");

    nome.append(input("Digite seu nome: "));
    curso.append(input("Curso você faz aqui no Senac: "));
    periodo.append(int(input("Período: ")));
    hobby.append(input("Um Hobby: "));

    resp = input("Deseja continuar? [s/n]");

    if "n" in resp or "N" in resp:
        continuar = False;

for pessoa in range(len(nome)):
    print(f"Prazer, eu sou o(a) {nome[pessoa]}. Atualmente estou no {periodo[pessoa]} ° semestre de {curso[pessoa]} e meu hobby é {hobby[pessoa]}");
