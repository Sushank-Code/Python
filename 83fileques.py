# Attempt question 82 and find line number of python location inlog file.

content=True
i=1

with open("log82.txt","r") as f:
    while content:
        content=f.readline().lower()

        if "python" in content:
            print(content)
            print("Python is present")
            print(i)
        i=i+1