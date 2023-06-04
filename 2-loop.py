# file name: 2-loop.py 
for x in range(1, 100+1) :
    if(x % 3 == 0 and x % 5 == 0):
        print("Couples", end=", ")
    elif(x % 3 == 0): 
        print("boys", end=", ")
    elif(x % 5 == 0): 
        print("girls", end=", ")    
    print(x, end=", ")
