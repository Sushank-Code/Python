# WAP to print sum of first n natural number using recursive function

def sum(n):
    if n==1:
       return 1
    else:
        return n + sum(n-1)

num = int(input("Enter the no"))
print(sum(num))