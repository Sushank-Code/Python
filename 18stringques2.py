a=input("Enter your name\n")
b=input("Enter the date\n")
letter='''   Dear Name
                  You are selected
                    Date:  date'''
letter=letter.replace("Name",a) 
letter=letter.replace("date",b)  
print(letter)
