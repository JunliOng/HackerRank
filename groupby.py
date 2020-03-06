# groupby example. groups similar neighboring elements (eg 1, 222, 3, 11) and returns (count,key) pair
# INPUT: 1222311
# OUTPUT: (1,1) (3, 2) (1, 3) (2, 1)

from itertools import groupby

string = input()
    
for key, group in groupby(string):
    count = 0 
    for i in group:
        count += 1

    print( "(" + str(count) + "," + " " + str(key) + ")" , end = " ")