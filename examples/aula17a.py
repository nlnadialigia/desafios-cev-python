num = [2, 5, 9, 1]
print(num)
num[2] = 3
print(num)
num.append(7)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
num.insert(2, 0)
print(num)
print(f'Essa lista tem {len(num)} elementos.')
num.pop()
print(num)
num.insert(2, 2)
print(num)
num.remove(2)
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)



