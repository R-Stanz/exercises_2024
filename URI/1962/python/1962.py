n = int(input())
for i in range(n):
    year = int(input())
    if (year < 2015):
        diff = 2015 - year
        print(str(diff) + " D.C.")
    else:
        diff = year - 2014
        print(str(diff) + " A.C.")
