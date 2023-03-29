def hex():
    n = int(input("ENter size of hexagon:"))
    for i in range(0, n):
        if n == 1:
            print("*")
        elif n == 2:
            print("* *")
        elif n == 3:
            print("* * *")
        else:
            print("*")
hex()
