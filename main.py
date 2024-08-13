from itertools import groupby

def Compress(S):

    s = groupby(S)
    for i, c in s:
        print((len(list(c)), int(i)), end=" ")
        
if __name__ == '__main__':
   
    S = input()
    resl = Compress(S)
