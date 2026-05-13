#Calculo de IMC simples
bancoSaude = [];
continuar = True;

while continuar:
    paciente = [];

    paciente.append(input("Nome do paciênte: "));
    paciente.append(float(input("Digite sua altura (m): ")));
    paciente.append(float(input("Digite seu peso (kg): ")));

    imc = paciente[2]/(paciente[1]**2);
    paciente.append(imc);

    bancoSaude.append(paciente);

    resp = input("Deseja cadastrar mais uma compra? [s/n] ");

    if resp.upper() == "N": continuar = False;

for i in range(len(bancoSaude)):
    print(f"{bancoSaude[i][0]}, seu IMC é de {bancoSaude[i][3]:.4f}")
    