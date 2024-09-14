try:
    a = int(input("Enter any number: "))
    print(f"Multiplication table of {a} is:")
    for i in range(1,6):
        print(f"{a} X {i} = {a *i}")
except ValueError as e:
    print("Number entered is not interger")

print("End of program")   

'''try:
    num = int(input("Enter any number: "))
    print(num)
except:
    print(" Not integer") '''

