# 1.
Quan = ['BĐ', 'BTL', 'CG', 'ĐĐ', 'HBT']
Dan_so = [247100, 333300, 266800, 420900, 318000]

# 2. Tìm quận có dân số lớn nhất và nhỏ nhất
max = Dan_so[0] # 247100
min = Dan_so[0] # 247100
for i in Dan_so:
    if i > max:
        max = i
    if i < min:
        min = i
print("Quận có dân số lớn nhất: ", Quan[Dan_so.index(max)])
print("Quận có dân số nhỏ nhất: ", Quan[Dan_so.index(min)])

