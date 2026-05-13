#Sistema de médias simples
bancoAluno = [];
continuar = True;
while continuar:
    aluno = [];
    aluno.append(input("Digite o nome do aluno: "));
    aluno.append(float(input("Digite a primeira nota: ")));
    aluno.append(float(input("Digite a segunda nota: ")));
    aluno.append(float(input("Digite a terceira nota: ")));

    somaNotas = 0; 
    
    for i in range(3):
        somaNotas += aluno[i + 1];

    media = somaNotas/ 3;
    aluno.append(media);

    bancoAluno.append(aluno);

    resp = input("Deseja continuar? [s/n]");

    if resp.upper() == "N": 
        continuar = False;


for i in range(len(bancoAluno)):
    print(f"O(A) estudante {bancoAluno[i][0]} teve um média de {bancoAluno[i][4]}")
    