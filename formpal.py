import sys

def recurr(input):
    if (len(input) == 1):
        return 0
    if(len(input) == 2):
        return 0 if (input[0] == input[1]) else 1
    if input[0] != input[-1]:
        return min(recurr(input[0:len(input) - 1]), recurr(input[1:len(input)])) + 1
    else:
        return recurr(input[1:len(input) - 1])



print(recurr("aab"))
print(recurr("aba"))
print(recurr("abcd"))
