//  Como segunda etapa, gostaríamos de ver alguns códigos gerados por ti.
//  Sendo assim, pedimos que tu crie códigos para os seguintes desafios.
//  1 - Fibonnaci
//      -- Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função), e retornar o valor correspondente desse número na sequencia fibonnaci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.
//      --- Criar uma função recursiva que resolva fibonacci
//      --- Criar uma função linear que resolva fibonnaci

import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        int validFibonacci = validateInput();

        System.out.println("\nResolução da sequência de Fibonacci por função recursiva em Java.");
        System.out.println("O valor do " + validFibonacci + "º número é " + recursiveFibonacci(validFibonacci));

        System.out.println("\nResolução da sequência de Fibonacci por função linear em Java.");
        System.out.println("O valor do " + validFibonacci + "º número é " + linearFibonacci(validFibonacci));
    }

    public static int validateInput() {
        int checkNumber = 0;
        boolean isValidInput = false;
        Scanner scanner = new Scanner(System.in);

        while (!isValidInput) {
            try {
                System.out.print("Qual n-ésimo dígito da sequência de Fibonacci deseja? ");
                checkNumber = scanner.nextInt();

                if (checkNumber > 0) {
                    isValidInput = true;
                } else {
                    System.out.println("Inserir número positivo.");
                }
            } catch (java.util.InputMismatchException e) {
                System.out.println("Inserir número positivo inteiro.");
                scanner.nextLine();
            }
        }

        return checkNumber;
    }

    public static int recursiveFibonacci(int n) {
        if (n == 1 || n == 2) return 1;
        return recursiveFibonacci(n - 1) + recursiveFibonacci(n - 2);
    }

    public static int linearFibonacci(int n) {
        if (n == 1 || n == 2) return 1;

        int current = 1;
        int previous = 1;
        for (int i = 3; i <= n; i++) {
            int newFib = current + previous;
            previous = current;
            current = newFib;
        }

        return current;
    }
}
