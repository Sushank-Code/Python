#WAP to find greatest of the four number.
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
num3=int(input("Enter the number3:"))
num4=int(input("Enter the number4:"))

if(num1>num2 and num1>num3 and num1>num4):
    print(num1,"is greater")
elif(num2>num1 and num2>num3 and num2>num4):
    print(num2,"is greater")
elif(num3>num1 and num3>num2 and num3>num4):
    print(num3 ,"is greater")
elif(num4>num1 and num4>num2 and num4>num3):
    print(num4,"is greater")
else:
    print("Nothing remain")

