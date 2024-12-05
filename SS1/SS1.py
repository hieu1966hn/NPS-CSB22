# Xuất dữ liệu lên màn hình terminal
# print("Hello World!!!")
# print('Welcome User, ', end='\n')
# print('mindx', 'edu', 'vn', sep='.')
# print("{} + {} = {}".format(1,2,3))
# print(100)


## Ví dụ
# name = "Nguyễn Trung Hiếu"
# height = 1.79
# print(name)
# print("{} is {} meters tall".format(name, height))

### Ví dụ với input()
# print("Input your name: ", end="")
# name = input()
# print("Input your age: ", end="")
# age = input() ## Tuổi nhập vào là kiểu String
# ### Thay đổi từ String => Int: Sử dụng hàm int(<biến>)
# age = int(age)

# print(name, age + 27)



##### Yêu cầu đề bài thư viện TURTLE;
### 1. Vẽ tam giác đều bằng TURTLE
from turtle import *

forward(100)
right(120)
forward(100)
right(120)
forward(100)
right(120)

mainloop() ## không bị tự động tắt chương trình
