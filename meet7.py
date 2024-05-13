# tabel kebenaran
# nod and xor

#not
print("*** Logika NOT********")
x = False
y = not x
print('value x =', x)
print('**********NOT')
print('value y =', y)

# OR (semua bernilai true asalkan ada truenya)
# berlaku untuk prempuan
print("***Logika OR*****")
x = False
y = False
z = x or y
print(x, 'OR', y, '=', z)
x = False
y = True
z = x or y
print(x, 'OR', y, '=', z)
x = True
y = False
z = x or y
print(x, 'OR', y, '=', z)
x = True
y = False
z = x or y
print(x, 'OR', y, '=', z)

# AND (bernilai true,ketika kedunya true)
# berlaku untuk lelaki
print("*****Logika AND*****")
x = False
y = False
z = x and y
print(x, 'AND', y, '=', z)
x = False
y = True
z = x and y
print(x, 'AND', y, '=', z)
x = True
y = False
z = x and y
print(x, 'AND', y, '=', z)
x = True
y = True
z = x and y
print(x, 'AND', y, '=', z)

# AND ( jika keduanya sama, hasilnya false sisanya benar)
#
print("*****Logika XOR*****")
x = False
y = False
z = x ^ y
print(x, '', y, '=', z)
x = False
y = True
z = x ^ y
print(x, '', y, '=', z)
x = True
y = False
z = x ^ y
print(x, '', y, '=', z)
x = True
y = True
z = x ^ y











