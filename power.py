#Write a program that takes an integer as input and returns true if the input is a power of two.
def is_power_of_two(n):
    if n <= 0:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

num = int(input("Enter a number: "))
print(is_power_of_two(num))
