def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


number = int(input("Enter a number: "))

while number != 1:
    number = collatz(number)
    print(number)
