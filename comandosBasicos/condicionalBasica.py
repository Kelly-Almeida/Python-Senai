# Condicionais básicas
nome = input("Digite o nome do usuário: ")
salario = float(input("Digite o salário do usuário: "))
print(f"O salário do(a) {nome} é de R${salario}")
if salario >= 1000:
  print(f"O(A) {nome} ganha bem!!!")
else:
  print(f"O(A) {nome} ganha pouco!!!")