# PROGRAMA DE CALCULO DE QUANTO CONTRIBUIR EM CHUREAS
print("----------------------------------\n");
print("\tSistema de racha do churras\n");
print("----------------------------------\n");
quantP = int(input("Digite a quantidade de pessoas que vão ao churrasco: "));

#Calculo de quantidade necessária de alimento
carneNecess = quantP * 0.3;
frangoNecess = quantP * 0.15;
linguicaNecess = quantP * 0.2;

print(f"Quantidade necessária: \nCarne: {carneNecess:.2f}kg \nLinguiça: {linguicaNecess:.2f}kg \nFrango: {frangoNecess:.2f}kg");

#Calculo do custo
carneCusto = 50 * carneNecess
frangoCusto = 22 * frangoNecess
liguicaCusto = 28 * linguicaNecess

print(f"Custo total: \nCarne R$ {carneCusto:.2f} \nLinguiça: R${liguicaCusto:.2f} \nFrango: R${frangoCusto:.2f}");

#Custo total
custoTotal = carneCusto + frangoCusto + liguicaCusto;
custoP = custoTotal/ quantP;
print(f"Custo total do churrasco: {custoTotal:.2f} \nCada pessoa deve contribuir com: R$ {custoP:.2f}");
