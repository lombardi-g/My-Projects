# Como segunda etapa, gostaríamos de ver alguns códigos gerados por ti.
# Sendo assim, pedimos que tu crie códigos para os seguintes desafios.
# 1 - Fibonnaci
#     -- Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função), e retornar o valor correspondente desse número na sequencia fibonnaci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
#     --- Criar uma função recursiva que resolva fibonacci
#     --- Criar uma função linear que resolva fibonnaci

def validate():
    while True:
        try:
            check_number = int(input("Qual n-ésimo dígito da sequência de Fibonacci deseja? "))
            if check_number > 0:
                # print(fibonacci_n) #test
                return check_number
            else:
                print("Inserir número positivo.")
        except ValueError:
            print("Inserir número positivo inteiro.")
     
def recursive_fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci (n-2)

def linear_fibonacci(n):     
    if n==1 or n==2:
        return 1
    
    current = 1
    previous = 0
    for _ in range(2,n+1):
        new = current + previous
        previous = current
        current = new
    return current

valid_fibonacci = validate()
print("\nResolução da sequência de Fibonacci por função recursiva em Python.")
print(f'O valor do {valid_fibonacci}º número é {recursive_fibonacci(valid_fibonacci)}')

print("\nResolução da sequência de Fibonacci por função linear em Python.")
print(f'O valor do {valid_fibonacci}º número é {linear_fibonacci(valid_fibonacci)}\n')