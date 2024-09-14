f = open("poem75ques.txt","r")
a = f.read()
if("sun" in a):
    print("It is present")
else:
    print("Nope")
f.close()

# Create a file containing poem and find whether a particular word is present in the file or not.