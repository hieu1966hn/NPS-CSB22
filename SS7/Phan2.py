color_list = ["blue", "red", "teal", "green"]

#2 Sử dụng list ở Phần 1, viết chương trình hỏi người dùng muốn xoá màu nào trong danh sách.
# print("Input a color to remove: ")
# remove_color = input() ## màu muốn xoá
# # - Nếu người dùng nhập số, thực hiện xoá theo vị trí.
# if remove_color.isdigit(): ## isdigit() kiểm tra xem chuỗi có phải là số không => True/False
#     color_list.remove(color_list[int(remove_color)]) ## xoá màu theo vị trí
#     print(color_list)

# # - Nếu người dùng nhập chữ, thực hiện xoá theo giá trị.
# else:
#     color_list.remove(remove_color) # xóa theo giá trị
#     print(color_list)
    
    
list_color = ['red', 'orange', 'yellow','green', 'blue', 'violet']

# Sử dụng turtle để vẽ một đường thẳng bao gồm các
# đoạn nhỏ nối liền nhau, mỗi đoạn có màu lần lượt là
# các màu trong danh sách ở Phần 1.

from turtle import *

shape("turtle")

for i in list_color:
    color(i)
    forward(50)
    penup()
    forward(25)
    pendown()

mainloop()



    
    