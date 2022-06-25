t = ()
for a in range(0, 5):
    x = int(input())
    t = t + (x,)

z = t[0]
print
for element in t:
    if element > z:
        z = element
    else:
        z = z
for element in t:
    if element < z:
        z = element
    else:
        z = z

