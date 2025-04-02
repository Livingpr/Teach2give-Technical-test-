#Write a program that takes an integer as input and returns an integer with reversed digit ordering.
def reverse_integer(n):
    reversed_num = 0
    is_negative = n < 0
    n = abs(n)  
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
    
    return -reversed_num if is_negative else reversed_num

num = int(input("Enter an integer: "))
print("Reversed:", reverse_integer(num))
