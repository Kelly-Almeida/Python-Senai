#Programa para calcular o valor final de uma compra com seu preço e cupom
bancoCompra = [];
continuar = True;

while continuar:
    compra = [];

    compra.append(input("Nome do comprador: "));
    compra.append(float(input("valor da compra: ")));
    compra.append(float(input("Porcentagem (%) de desconto de seu cumpo: ")));

    valorFinal = compra[1] - (compra[1] * (compra[2]/100));
    compra.append(valorFinal);
    bancoCompra.append(compra);

    resp = input("Deseja cadastrar mais uma compra? [s/n] ");

    if resp.upper() == "N": continuar = False;

for i in range(len(bancoCompra)):
    print(f"Olá {bancoCompra[i][0]}, sua compra de R${bancoCompra[i][1]:.2f} foi confirmada!\nFoi aplicado um desconto de {bancoCompra[i][2]:.2f}%.\nO total final ficou em R${bancoCompra[i][3]:.2f}.")
    