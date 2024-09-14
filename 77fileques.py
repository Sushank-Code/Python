# A file contain a word "Donkey" multiple times . You need to replace the word with ####
# by updating it inthe same file.

with open("sample71.txt","r") as f:
    data = f.read() 
data=data.replace("Donkey","#####")
print(data)

with open("sample71.txt","w") as f:
    f.write(data)
