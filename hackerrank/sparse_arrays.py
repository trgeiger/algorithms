"""
There are N strings. Each string's length is no more than 20 characters.
There are also Q queries. For each query, you are given a string, and
you need to find out how many times this string occurred previously.

Input Format

The first line contains N, the number of strings.
The next N lines each contain a string.
The N + 2nd line contains Q, the number of queries.
The following Q lines each contain a query string.

Sample Input

4
aba
baba
aba
xzxb
3
aba
xzxb
ab
Sample Output

2
1
0
Explanation

Here, "aba" occurs twice, in the first and third string.
The string "xzxb" occurs once in the fourth string, and "ab" does not occur at all.
"""

""" SOLUTION
"""

import sys


#clean input
inp = sys.stdin.readlines()
data = []
for line in inp:
    data.append(line.strip())


def splitInput(data):
    first = int(data[0])
    flist = []
    slist = []
    for i in range(1, first+1):
        flist.append(data[i])
    for i in range(first+2, first+2+int(data[first+1])):
        slist.append(data[i])
    return(flist, slist)

flist, slist = splitInput(data)

for i in slist:
    counter = 0
    for j in flist:
        if i == j:
            counter += 1
    print(counter)
