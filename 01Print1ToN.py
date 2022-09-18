#print 1 to n
#Recursion

def printOneToN(n):
    if n<=0:
        return
    printOneToN(n-1)
    print(n)


n = int(input("enter integer "))
printOneToN(n)