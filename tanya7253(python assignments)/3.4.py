def calculate_salary(basic_salary):
    if basic_salary >= 20000:
        da = 0.3 * basic_salary
        hra = 0.2 * basic_salary
    else:
        da = 0.2 * basic_salary
        hra = 0.1 * basic_salary
    return basic_salary + da + hra

def main():
    basic_salary = float(input("Enter the basic salary: "))
    total_salary = calculate_salary(basic_salary)
    print("Total salary (including DA and HRA):", total_salary)

if __name__ == "__main__":
    main()
