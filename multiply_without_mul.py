def helper(a,b,counter):
    if(counter==0):
        return 0
    return a + helper(a,b,counter-1)
def multiply(a,b):
    if(a==0 or b==0):
        return 0
    return helper(a,b,b)
print(multiply(7,0))
print(multiply(7,7))
print(multiply(7,8))



