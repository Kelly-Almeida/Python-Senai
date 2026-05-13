#Programa de conversão simples
continuar = True;
while continuar:
    real = float(input("Digite a quantidade de reis que quer converter par dolar: "));
    dolar = real/ 5.42;
    print(f"Valor em real R$ {real:.2f} \nValor em dólar $ {dolar:.2f}");

    resp = input("Deseja continuar convertendo? [s/n] ");
    
    if resp.upper() == "N": 
        continuar = False;

    