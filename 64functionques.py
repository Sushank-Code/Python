def convert(C):
    f=((C*180)/100)+32
    return f

num= convert(int(input("ENter celsius")))
print(num)

# Conversion of celsius into farenheit