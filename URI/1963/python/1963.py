str_numbs = input().split(" ")

a, b = [float(i) for i in str_numbs]

result = 100 * (b-a)/a
print("%.2f%%" % result)
