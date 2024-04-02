def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    num = float(input("Enter a number: "))
    print(f"The number {num} is {check_number(num)}")

if __name__ == "__main__":
    main()
