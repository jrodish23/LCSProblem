"""
Author: Jarrad Self
CS4306 Section 04
Project 2 - 12-4-22
"""

string_one = "GAGTAAG"  #Test Case #1
string_two = "GCGACG"  #LCS Should = GGAG

"""
string_one = "CTCAGGT"    #Test Case #2
string_two = "GTGAGGGGGA"  #LCS Should = TAGG
"""

"""
string_one = "AGGACGGTGAA"     #Test Case #3
string_two = "AATTTTTA"        #LCS Should = AATA
"""

x = len(string_one)
y = len(string_two)

Matrix = [[0 for i in range(y+1)] for j in range(x+1)]
get_LCS = [[0 for i in range(y+1)] for j in range(x+1)]

for i in range(x):
    for j in range(y):
        if string_one[i] == string_two[j]:
            Matrix[i+1][j+1] = Matrix[i][j] + 1
            get_LCS[i+1][j+1] = "3"
        elif Matrix[i][j+1] >= Matrix[i+1][j]:
            Matrix[i+1][j+1] = Matrix[i][j+1]
            get_LCS[i+1][j+1] = "1"
        else:
            Matrix[i+1][j+1] = Matrix[i+1][j]
            get_LCS[i+1][j+1] = "2"

for i in range(y+1):
    get_LCS[0][i] = '0'

for i in range(x+1):
    get_LCS[i][0] = '0'

ls1 = []

while True:
    if(get_LCS[x][y] == '0'):
        break
    elif (get_LCS[x][y] == "1"):
        x = x-1
    elif (get_LCS[x][y] == "2"):
        y = y-1
    elif (get_LCS[x][y] == "3"):
        ls1.append(string_one[x-1])
        x = x-1
        y = y-1

ls2 = []
i = len(ls1) - 1
for j in range(len(ls1)):
    ls2.append(ls1[i])
    i = i-1

print("Row Sequence: " ,string_one)
print("Column Sequence: " ,string_two)

for row in Matrix:
    print(" ".join(map(str,row)))

lcs = "".join(ls2)
print("LCS: {0}".format(lcs))

