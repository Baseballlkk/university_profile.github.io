list = []
for i in range(3):
    a = input('Please input number:\n')
    x = float(a)
    list.append(x)
list.sort(reverse = True)
print(list)