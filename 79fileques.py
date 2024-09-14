# WAP to copy the content of a one file into another file

with open("this.txt","r") as f:
    data=f.read()

with open("copy.txt","w") as f:
    f.write(data)