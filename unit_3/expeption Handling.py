# Try and Except block

n = int(input("Enter the numerator: "))
try:
    d = int(input("Enter the denominator: "))
    print(n/d)
except ZeroDivisionError as e:
    print(f'ZeroDivisionError: {e}')

n = int(input("Enter the numerator: "))
d = int(input("Enter the denominator: "))
print(n/d)


# Try except and else block

try:
    n = int(input("Enter a number: "))
    assert n%2 == 0
except:
    print("Not an even number")
else:
    print(n/4)
