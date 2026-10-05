def is_prime_number(result):
    if result < 2:
        return False
    
    for numbers in range(2, result):
        if result % numbers == 0:
            return False

    return True

result = int(input("Enter a number: "))
print(is_prime_number(result))
