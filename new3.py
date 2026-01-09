#in this we will learn about break and continue statements in loops
#break statement
for i in range(2,10):
    for j in range(2,i):
        if i%j==0:
            print(f"{i} equals {j} * {i//j}")
            break
        