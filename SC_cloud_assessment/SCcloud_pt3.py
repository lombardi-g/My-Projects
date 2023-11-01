# Como segunda etapa, gostaríamos de ver alguns códigos gerados por ti.
# Sendo assim, pedimos que tu crie códigos para os seguintes desafios.
# 2 - Números primos
#     -- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input), e retornar todos os números primos até o numero N. EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];
#     --- Criar uma função recursiva que resolva p
#     --- Criar uma função linear que resolva p

def validate():
    while True:
        try:
            check_number = int(input("Deseja ver os números primos até qual número? "))
            if check_number > 1:              
                return check_number
            else:
                print("Inserir número maior que 1.")
        except ValueError:
            print("Inserir número positivo inteiro.")

def recursive_prime(p, i=2, primes=None):
    if primes is None:
        primes = []

    if i <= p:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

        return recursive_prime(p, i + 1, primes)

    return primes   

def linear_prime(p):
    primes = []

    for num in range(2,p+1):
        is_prime = True
        for i in range(2, num):
            if num % i ==0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)

    return primes

valid_prime = validate()

print(f"\nSequência de números primos até {valid_prime} por função recursiva em Python.")
print(recursive_prime(valid_prime))

print(f"\nSequência de números primos até {valid_prime} por função linear em Python.")
print(linear_prime(valid_prime))