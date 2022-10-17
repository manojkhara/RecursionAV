# https://leetcode.com/problems/k-th-symbol-in-grammar/

"""
We build a table of n rows (1-indexed). 
We start by writing 0 in the 1st row. 
Now in every subsequent row, 
we look at the previous row and replace each occurrence of 0 with 01, 
and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

"""

"""
0
01
0110
01101001
"""


def kthGrammar(n: int, k: int) -> int:

    if n == 1 and k == 1:
        return 0

    mid = 2 ** (n-1) / 2

    if k > mid:
        return 1 - kthGrammar(n-1, k-mid)
    else:
        return kthGrammar(n-1, k)

print(kthGrammar(4,6))
