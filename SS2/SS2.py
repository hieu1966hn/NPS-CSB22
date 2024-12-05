## khai báo chuỗi cơ bản
str_1 = ''
str_2 = 'abc'
str_3 = 'MindX'
str_4 = 'embedded "double" quotes'
str_5 = "embedded 'single' quotes"
str_6 = '''Three single quotes'''
str_7 = """
Three
double
quotes"""

# print(str_1)
# print(str_2)
# print(str_3)
# print(str_4)
# print(str_5)
# print(str_6)
# print(str_7)

# print(str_2 + " " + str_3)


#### Truyền biến vào chuỗi: 
# truyen_bien = f"I am learning at {str_3} school"


## Đếm số ký tự có trong biến "truyen_bien"
# print(f'Số ký tự có trong biến "truyen_bien" là {len(truyen_bien)}')


### In ra ký tự X có trong biến "str_3"
# print(str_3[4])

### In ra ký tự "ind" bên trong biến "str_3"
# print(str_3[1:4])

### Kiểm tra kiểu dữ liệu của 2 biến sau:
# a = 'Hello World!'
# b = 123
# c = 12.0
# print(type(a))
# print(type(b))
# print(type(c))


### Toán tử số học: 
# a = 1
# b = 2
# print(a+b) 
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)
# print(a**b)
# print(a==b)



# Cú pháp thông thường: 
# count = 0
# count = count + 1
# budget = 100
# budget = budget*(1 + 5/100)
# print(budget)

# Cú pháp kết hợp
# count = 0
# count += 1

# budget = 100
# budget *= 1 + 5/100




### Chữa bài tập thực hành 

## Bài 1
# print('Nhập bán kính hình tròn')
# r = input() ## r đang là string
# r = float(r) ## ép kiểu dữ liệu về dạng Float
# Pi = 3.14
# print(f'Chu vi hình tròn là: {2*Pi*r}')
# print(f'Diện tích hình tròn là: {Pi*r**2}')

## Bài 2 
print("Nhập cạnh hình vuông")
a = input()
a = float(a)
## Viết căn bậc 2
import math
print(f'Độ dài đường chéo của hình vuông với cạnh {a} là: {math.sqrt(2)*a}') 
