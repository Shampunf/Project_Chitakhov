l = ["1 4 -2 5 9 4 65 64 89"]
f3 = open('data_22_1.txt', 'w')
f3.writelines(l)
f3.close()
b = l.split(' ')
print(b)
for i in l:
    if i % 2 == 0:
        a = []
        i += a
        print(a)
        print(i.count())

