# https://en.wikipedia.org/wiki/Tower_of_Hanoi

# Showing pretty output but hard to understand code than pevious one 

def towerOfHanoi(s:str, d:str, h:str, n:int):

    # Base Case    
    if n==0:
        return

    towerOfHanoi(s, h, d, n-1)     #sending n-1 plates from source to helper rod

    global counter
    counter += 1
    print(f"step {counter}: moving plate {n} from {s} to {d}")
    
    towerOfHanoi(h, d, s, n-1)     #sending n-1 plates from helper to destination

    return



#driver code

s = "Source"
h = "Helper"
d = "Destination"
n = 3

counter = 0

towerOfHanoi(s, d, h, n)

print(f"\ntotal {counter} steps required to transfer {n} plates")
