# Put a log file in file and find whether it contain 'python' or not

with open("log82.txt","r") as f:
    content=f.read().lower()

if "python" in content:
    print("Python is present")
else:
    print("Python is not present")