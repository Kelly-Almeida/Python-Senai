meta = input("Sua meta: ");
preco = float(input("Valor da meta: "));
salario = float(input("Digite seu salário: "));
despesas = float(input("Valor das dispesas: "));

valorSemDespesas = salario - despesas;
reserva = valorSemDespesas * 0.3;
valorSemReserva = valorSemDespesas - reserva;
tempoA = preco/valorSemReserva;

print(f"Meta: {meta}\nSalário: R${salario:.2f}\n\nSaldo após despesas: R${valorSemDespesas:.2f}\nReserva fixa (30%): {reserva:.2f}\nValor disponível para a meta: R$ {valorSemReserva:.2f}\nPrazo estimado para atingir a meta: {tempoA:.2f} meses")