number = int(input("Enter the number: "))

print("Multiplication table of", number)
for i in range(1, 11):
    print(number, "x", i, "=", number * i)
