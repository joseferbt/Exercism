"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = "sublist"
SUPERLIST = 'superlist'
EQUAL = 'EQUAL'
UNEQUAL = 'uniqual'

def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    lone = len(list_one)
    ltwo = len(list_two)
    if lone == 0:
        return SUBLIST
    if ltwo == 0:
        return SUPERLIST
    if check(list_one,list_two,lone,ltwo) :
        return SUBLIST
    if check(list_two,list_one,ltwo,lone):
        return SUPERLIST
    return UNEQUAL
    
  
def check(l1,l2,lone,ltwo):
    try:
        first = l2.index(l1[0])
        found = True
        while(found):
            count = 0
            for i in range(lone):
                if l2[first+i] != l1[i]:
                    break
                count += 1
            if count == lone:
                return True
            first += 1+l2[first+1:].index(l1[0])
    except:
        return False    