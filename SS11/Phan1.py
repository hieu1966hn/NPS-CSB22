# Khởi tạo thành công 1 dictionary với các key và value tương ứng
Kho = { 
    "HP": 20,
    "DELL": 50,
    "MACBOOK": 12,  
    "ASUS": 30
}

# print("Available MACBOOKs: {}".format(Kho["MACBOOK"]))

## Người dùng nhập vào hãng máy tính
hang_may_tinh = input("Người dùng nhập vào 1 hãng máy tính: ")
if hang_may_tinh in Kho: # kiểm tra hãng đó có là khóa trong Kho không?
    print("Available {}: {}".format(hang_may_tinh, Kho["MACBOOK"]))
