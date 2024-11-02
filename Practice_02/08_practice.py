Given_no = 25

is_prime = True

if Given_no > 1 :
    for i in range(2, Given_no):
        if (Given_no%i) == 0:
            is_prime = False
            break

if is_prime:
    print("this No. is prime")
else:
    print("Not a prime")