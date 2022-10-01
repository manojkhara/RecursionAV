#Recursion
#Sort an list using Recursion
# youtube Link given below
#https://www.youtube.com/watch?v=AZ4jEY_JAVc&list=PL_z_8CaSLPWeT1ffjiImo0sYTcnLzo-wY&index=6&ab_channel=AdityaVerma

def sorting(lst):
    # base case
    if(len(lst)<=1):
        return
    #code
    temp=lst.pop()   #store last element of list
    sorting(lst)     #keep removing last element of list until only one element remains
    insertion(lst,temp) #insert function


def insertion(lst,temp):
    if(lst == [] or lst[len(lst)-1]<temp):      # if no element remains in list then append or temp is greater than last element
        lst.append(temp)
        return
    x = lst.pop()    #insertion at proper position will only happens if there are no elements present in the list
    insertion(lst,temp)
    lst.append(x)     #inserting after all the above commands destacks

lst=[5,3,2,4,-5,1,6,-1,9,0]
sorting(lst)
print(lst)