num=int(input("Enter any number:"))
if(num==1):
    print("Not prime number")
elif(num>1):
    for n in range(2,num):
        if(num%n==0):
            print(num, "is not prime number" )
            break
    else:
            print(num,"is prime number")
