#Recursion
#Print n to 1
# 5 --> 5 4 3 2 1

def printNtoOne(n):
    if n<=0:
        return

    print(n)
    printNtoOne(n-1)


# driver code
n = int(input("enter an integer "))
printNtoOne(n)