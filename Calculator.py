a = input("input first number: ")
a = int(a)
b = input("input second number: ")
b = int(b)
print("----press keys for operator(+,-,/,*,%)-----")
operation = input("operation to be performed: ")

if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "/":
    print(a / b)
elif operation == "*":
    print(a * b)
elif operation == "%":
    print(a % b)
else:
    print("Invalid Operation")



