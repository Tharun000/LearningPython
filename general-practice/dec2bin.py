# This program is to convert numbers from base 10 to base 2
# José C.S. Curet

base = 2
number = int(input("Enter number: "))

remainder = []
while number > 0:
    remainder.append(str(number % base))
    number //=base

def reverse_and_string(remainder):
    _to_string = " "
    remainder.reverse()

    return(_to_string.join(remainder))

print(reverse_and_string(remainder))