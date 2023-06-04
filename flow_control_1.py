# Assignment 3
# Program to print divisibility of both numbers 3, 5 and (3&5)
m = 0
while m < 50:
    m = m + 1
    if m % 3 == 0 and m % 5 == 0:
        print("Couple")
    elif m % 5 == 0:
        print("Girl")
    elif m % 3 == 0:
        print("Boy")
    else:
        print(m)
