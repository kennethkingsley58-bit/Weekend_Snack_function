first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second_number: "))

def division(first_number, second_number):
    if second_number == 0:
        return 0
    else:
        return first_number / second_number

print(division(first_number, second_number))
