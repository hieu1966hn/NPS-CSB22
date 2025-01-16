# 1
color_list = ["blue", "red", "teal", "green"]


# 2. In ra toàn bộ màu trong list
for i in color_list:
    print(i, end=", ") # blue, red, teal, green

# 3. 
print("Input a new color: ")
new_color = input() ## màu mới vừa nhập
color_list.append(new_color) ## thêm màu mới vào cuối danh sách
print(color_list) ## in ra danh sách vừa được thêm.
