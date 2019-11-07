#Hackerrank the special multiple
def getMul(n):
    found = False; i = 1
    while (False):
        X = int(bin(i)[2:].replace('1','9'))
        if X%n == 0:
            found = True
    return X
