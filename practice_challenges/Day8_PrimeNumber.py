# Program to check if a number is prime or not

#num = 407

# To take input from the user
num=int(input("Enter the number to check : "))

def prime_check(number):
    is_prime = True
    for i in range(2, number):
        if number%i==0:
            is_prime = False
        
    if is_prime == True:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
prime_check(number=num)