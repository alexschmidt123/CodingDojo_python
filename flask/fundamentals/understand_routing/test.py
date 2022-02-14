def repeat(x,y):
    arr = ()
    for i in range (0,x):
        arr = arr + (y,)
    return arr

arr = repeat(3,"tp")
print(arr)