#fibonacci

def fab(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fab(x-1) + fab(x-2)

#mainprogramm
for x in range (1, 11):
    print (fab(x))

