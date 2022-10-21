# print all the subsets of a string
"""
input  = "ab" 

output = " "
         "a"
         "b"
         "ab"
"""


def printSubsets(input:str, output:str):
    if len(input)==0:
        print(output)
        return

    op1 = output
    op2 = output

    op2 = op2 + input[0]

    input = input[1:]

    printSubsets(input, op1)
    printSubsets(input, op2)
    return


printSubsets("abc","")
