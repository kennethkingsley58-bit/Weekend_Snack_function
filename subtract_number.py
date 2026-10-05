first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

def subtract (first_number, second_number):
    if first_number > second_number:
        print(first_number - second_number)
    else:
        print(second_number - first_number)

print(first_number - second_number)
