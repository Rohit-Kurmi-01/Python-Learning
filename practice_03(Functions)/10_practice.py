given_number = 5

def fact(number):
    if number == 1 : return 1
    factorial = number * fact(number-1)
    return factorial

solution = fact(given_number)

print(solution)