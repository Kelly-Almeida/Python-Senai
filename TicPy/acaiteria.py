acaiP = int(input("Quantidade de açaís P: "));
acaiM = int(input("Quantidade de açaís M: "));
acaiG = int(input("Quantidade de açaís G: "));
desconto = float(input("Desconto aplicado (%): "));

total = (acaiG * 13.5 + acaiM * 15 + acaiP * 17.5) * (1 - (desconto/100));

print(f"Desconto de {desconto}%\nTotal R$ {total}")