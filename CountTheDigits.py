n = int(input("Enter a number: "))
count = 0
n = abs(n)
if n == 0:
    count = 1
else:
    while n > 0:
        count += 1
        n //= 10
print("Number of digits =", count)