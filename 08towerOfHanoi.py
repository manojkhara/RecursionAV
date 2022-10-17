# https://en.wikipedia.org/wiki/Tower_of_Hanoi


def towerOfHanoi(s:str, d:str, h:str, n:int):
    if n==1:
        print(f"moving plate {n} from {s} to {d}")
        return

    towerOfHanoi(s, h, d, n-1)

    print(f"moving plate {n} from {s} to {d}")
    towerOfHanoi(h,d,s,n-1)

    return



#driver code

s = "Source"
h = "Helper"
d = "Destination"
n = 4

towerOfHanoi(s, d, h, n)
