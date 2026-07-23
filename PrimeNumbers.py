number = int(input("Enter a number: "))
if number > 1:
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        print("Prime number")
    else:
        print("Not a prime number")
else:
    print("Not a prime number")