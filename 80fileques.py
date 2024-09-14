# WAP to find out whether two files are identical or not.

file1="this.txt"
file2="copy.txt"

with open("this.txt","r") as f:
    data1= f.read()

with open("copy.txt","r") as f:
    data2= f.read()

if(data1==data2):
    print("They are identical")
else:
    print("They are not identical")
