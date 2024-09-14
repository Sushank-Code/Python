def greatest(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print("The greatest is",num1)                  # WAP to find greatest among no
    elif(num2>num1 and num2>num3):
        print("The greatest is",num2)
    elif(num3>num2 and num3>num1):
        print("The greatest is",num3)
    else:
        print("All are same")
    
num1=int(input("Enter any no"))
num2=int(input("Enter any no"))
num3=int(input("Enter any no"))
greatest(num1,num2,num3)