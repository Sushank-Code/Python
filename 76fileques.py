# wap to print mulitplication table from 1 to 3 in different file by making folder.

for i in range(1,4):
    with open(f"tables/multiplication of {i}","w") as f:
        for j in range(1,11):
            t=f"{i} X {j} = {i*j}\n"
            f.write(t)
    
    