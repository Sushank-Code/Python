'''def factorial(num):
    fact=1
    for i in range(1,num):
        fact=fact * num
        num = num - 1
    return fact  

num=factorial(int(input("ENter any no")))           # Factorial using function
print(num)'''


# Factorial  using recursive fuction
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n* factorial_recursive(n-1)

num=int(input("ENter any no"))
f=factorial_recursive(num)
print(f)