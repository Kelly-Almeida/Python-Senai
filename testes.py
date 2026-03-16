#Operadores relacionais

n1 = 5
n2 = 7
print(f"n1 = {n1} e n2 = {n2}")
print(f"n1 == n2: {n1 == n2}")
print(f"n1 != n2: {n1 != n2}")
print(f"n1 > n2: {n1 > n2}")
print(f"n1 < n2: {n1 < n2}")
print(f"n1 >= n2: {n1 >= n2}")

#Operadores lógicos

n1 = 5
n2 = 7
nome = "Kelly"

print(f"n1 = {n1}, n2 = {n2} e nome = {nome}")

print(f" n1 é igual a n2 e n1 é maior ou igual a n2: {n1 == n2 and n1 >= n2}")
print(f" n1 é diferente de n2 ou n1 é maior ou igual a n2: {n1 != n2 or n1 >= n2}")
print(f" n1 não é igual a n2: {not n1 == n2}")
print(f" 'y' está em nome: {'y' in nome}")
print(f" 'll' não está em nome: {'ll' not in nome}")