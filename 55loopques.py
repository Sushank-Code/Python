num = int(input("Enter the number to be multiplicated"))
for i in range(10,0,-1):
    #print(str(num) + "X" + str(i) + "=" + str(num*i))
   mul= f"{num}X{i}={num*i}"
   print(mul)                       # reversed multiplication using for loop
      

'''num = int(input("Enter the number to be multiplicated"))
for i in range(1,11):
    #print(str(num) + "X" + str(i) + "=" + str(i*num))
   mul= f"{num}X{i}={num*i}"
   print(mul)               ''' #multiplication using for loop  