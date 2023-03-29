def cal():
    c = int(input("Enter score for test1:"))
    d = int(input("Enter score for test2:"))
    e = int(input("Enter score for test3:"))
    a = (c + d + e) / 3
    if a >= 90:
        print(f"The Grade for score {a} is  A")
    elif 80 <= a < 90:
        print(f"The Grade for score {a} is  B")
    elif 70 <= a < 80:
        print(f"The grade for score {a} is  C")
    elif 60 <= a < 70:
        print(f"The grade for score {a} is  D")
    else:
        print(f"The grade for score {a} is  E")

cal()