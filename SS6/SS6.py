## khởi tạo 1 danh sách
sports = ['bóng đá', 'bóng rổ', 'bơi lội']
### vị trí     0          1          2

### in ra terminal
# print(sports)


### Truy vấn giá trị thông qua vị trí 
# print(sports[2])


### Đếm số phần tử có trong list: len(list)
# print(len(sports))

### Thêm phần tử vào danh sách: list.append(item1, item2, ...)
sports.append("bóng bàn")
# print(sports) ### Đã có bóng bàn ở vị trí cuối cùng

## Thêm phần tử vào vị trí chỉ định: list.insert(index, item)
sports.insert(1, "bóng chày")
# print(sports) ### Đã có bóng chày ở vị trí số 1

## Thêm vào 1 danh sách: list.extend(list2)
sport2s = ['trượt tuyết', 'bóng chuyền']
sports.extend(sport2s)
# print(sports) ### Đã có danh sách 2 được thêm ngay sau phần tử cuối của danh sách 1.


####### Tìm vị trí phần tử: biết "giá trị" => tìm "vị trí": list.index("giá trị") => vị trí giá trị đó trong list


####### Xóa phần tử: list.remove(giá_trị)
sports.remove("trượt tuyết")
# print(sports) ### Đã xóa trượt tuyết khỏi danh sách


###### Yêu cầu: Duyệt danh sách | Loại bỏ các môn thể thao có từ "bóng" => in ra ds mới

#### C1: lặp qua index (chỉ mục - vị trí)
# for i in range(len(sports)): 
#     print(i) # i - vị trí các phần tử
    
    
#### C2: lặp qua phần tử
# for j in sports: 
#     print(j) # j - các phần tử trong danh sách 


#### C3: lặp qua index và phần tử
# for index, element in enumerate(sports): 
#     print(index, element, end=" ") ## end = " " cho phép em viết trên 1 dòng


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr3 = arr.copy()

## 2 gia tri dau tien: index: 0, 1
dem = 0 
for i in range(len(arr3)):
    if dem < 2:
        temp = arr3[0]
        arr3.remove(arr3[0])
        arr3.append(temp) ## them phan tu so 0 vao cuoi danh sach
        dem = dem + 1
    else:
        break
    
print(arr3)


