num = 0

while num < 5:
    print(num)
    num += 1
else:
    print("Loop completed successfully!")

print("\nAfter the loop")

num = 0

while num < 5:
    print(num)
    num += 1
    if num == 3:
        break
else:
    print("Loop completed successfully!")

print("\nAfter the loop")
