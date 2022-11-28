numb = int(input("Please enter number: "))

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number%i == 0:
            is_prime = False
    if is_prime:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is not prime")

prime_checker(numb)