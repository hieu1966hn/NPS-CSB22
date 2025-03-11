### Xử lý file

# Tạo file
# f = open("./SS12/sample.txt",'x')

# f.close()


## Ghi file: Thêm nội dung vào trong file: Cách thứ 2 mở file
# with open("./SS12/sample.txt",'w') as f:
#     f.write("First line\n")
#     f.write("Next line\n")
#     f.write("Another line\n")

# print("Thoát khỏi with")

## Ghi đè nội dung trong file: mode 
# with open("./SS12/sample.txt",'a') as f:
#     f.write("Append line with a mode\n")



## Xóa file đã tạo
import os

# if os.path.exists("./SS12/sample.txt"): ## kiểm tả file có tồn tại hay không?
#     os.remove("./SS12/sample.txt") ## dòng này dùng riêng cũng được

    
## Chữa bài 2: 
input_file_name = input("Mời người dùng nhập tên file: ")
# if os.path.exists("./SS12/{}".format(input_file_name)):
#     with open("./SS12/{}".format(input_file_name)) as f:
#         print(f.read())



### Cách 2
if os.path.exists("./SS12/{}".format(input_file_name)):
    f = open("./SS12/{}".format(input_file_name))
    print(f.read())
    f.close()
    
else:
    print("File not found!!!")