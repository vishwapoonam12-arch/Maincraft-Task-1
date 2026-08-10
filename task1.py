#Question 1 (sum of two numbers)

def sum_two_numbers(a, b):
    return a+b

n1=int(input("Enter first number: "))
n2=int(input("Enter second number: "))
sum=sum_two_numbers(n1, n2)




#Question 2 (Odd or even checker)

def odd_even_checker(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

num=int(input("Enter a number: "))
odd_or_even=odd_even_checker(num)






#Question 3 (Factorial of a number)

fact=1
def factorial(num):
    for i in range(num,1,-1):
        fact*=i
    return fact

n=int(input("Enter a number:"))
fact=factorial(n)





#Question 4 (Fibonacci series)

def fibonacci_series(limit):
    a, b = 0, 1
    while a <= limit:
        print(a, end=" ")
        a, b = b, a + b

limit = int(input("Enter the limit for Fibonacci series: "))
fibonacci_series(limit)




#Question 5 (String reverse)

def string_reverse(s):
    return s[::-1]

input_string = input("Enter a string: ")
reversed_string = string_reverse(input_string)
print("Reversed string:", reversed_string)




#Question 6 (Palindrome checker)

def is_palindrome(s):
    return s == s[::-1]

input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")





#Question 7 (Leap year checker)

def leap_year(year):
    if(year % 4 == 0 and year % 400 ==0):
        return True
    else:
        return False

year = int(input("Enter a year: "))
if leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")




#Question 8 (Armstrong number checker)

def armstrong(num):
    
    digits = str(num)
    n = len(digits)

    sum = 0
    for d in digits:
        sum = sum + int(d) ** n
        return sum


num = int(input("Enter a number: "))
check_sum = armstrong(num)
if check_sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")



    