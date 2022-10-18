# https://en.wikipedia.org/wiki/Tower_of_Hanoi

"""
For n = 3 plates on Source

step 1: moving plate 1 from Source to Destination
step 2: moving plate 2 from Source to Helper
step 3: moving plate 1 from Destination to Helper
step 4: moving plate 3 from Source to Destination
step 5: moving plate 1 from Helper to Source
step 6: moving plate 2 from Helper to Destination
step 7: moving plate 1 from Source to Destination

"""

def towerOfHanoi(n:int,  source :str, helper:str, destination:str):

    global counter
    counter += 1

    # Base Case    
    # when only last one plate remains on the source rod
    # transfer it to destination
 
    if n == 1:
        print(f"moving plate {n} from {source} to {destination} ")
        return

    towerOfHanoi(n-1, source, destination, helper)     #sending n-1 plates from source to helper rod

    print(f"moving plate {n} from {source} to {destination}")
    
    towerOfHanoi(n-1, helper, source, destination)     #sending n-1 plates from helper to destination

    return

#driver code
n = int(input("Enter number of plates:  "))     #don't enter high number stack will overflow
counter = 0
towerOfHanoi(n, "Source", "Helper", "Destination")
print(f"\ntotal {counter} steps required to transfer {n} plates")     # steps = (2 ** n) - 1 (but here counting using counter)
