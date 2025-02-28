#### Khai báo Dictionary
dict_1 = {} # khai báo dictionary rỗng

dict_2 = {
    "name": "Dương",
    "age": 2009,
    'wallet': 1000000,
    "12": ["Dương", "Thầy Hiếu"]
}


## In ra nhãn "name": lấy ra giá trị bên trong ngăn tủ 'name"
print(dict_2["name"])
print(dict_2["12"])


## Kiểm tra "key" có trong dictionary không?
print('name' in dict_2) # True/False


#### Lặp qua key
# for key in dict_2:
#     # print(key) # in ra khóa
#     print(dict_2[key]) # in ra value theo key
    
#### Lặp qua key và value
# for key, value in dict_2.items():
#     print(key, value, end=" ")

#### thêm phần tử
dict_2["sport"] = ["cầu lông", 'gym']

#### Xóa phần tử theo khóa
dict_2.pop('age')

print(dict_2)


#### Sao chép dictionary
dict_copy = dict_2.copy()