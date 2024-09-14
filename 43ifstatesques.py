#WAP to find out whether the student is failed or pass.
nepali=int(input("Enter the mark of Nepali:"))
math=int(input("Enter the mark of Math:"))
science=int(input("Enter the mark of science:"))

if(nepali>=33 and math>=33 and science>=33):
    print("You are pass")
elif((nepali+science+math)/3 >=40):
    print("You are pass")
else:
    print("You Failed")