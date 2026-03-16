# Media com quantidade variavel
def media (quantNum):
    soma = 0
    i = 0
    while i < quantNum:
        print(f"Digite o {i + 1}º número: ")
        num = float(input())
        soma += num
        i += 1
    print(f"A média dos números é: {soma / quantNum}")


media(5)