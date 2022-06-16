flag = False
def primenumbers(x):
    if x > 1:
        for y in range(2,x):
            if (x % y) == 0:
                flag = True
if flag:
    print("is not a prime number")
else:
    print("is a prime number")
