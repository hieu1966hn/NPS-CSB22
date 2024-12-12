## Thực hành cơ bản với if
# a = 200
# b = 300
# if a<b:
#     print(f"{a} là số nhỏ hơn {b}")


## Chữa bài thực hành 1
# print("Mời người dùng nhập 1 số nguyên n: ")
# n = int(input()) ## 4 input() trả về là 1 String. => String -> Int

# if n%2 == 0:
#     print(f"{n} is even")
# if n%2 != 0:
#     print(f"{n} is odd")


## Chữa bài thực hành 2
# print("Mời người dùng nhập 1 số thực n: ")
# n = float(input()) # 5.0
# if n == int(n):
#     print(f"{int(n)} là số nguyên")


### Chữa bài 3
print("Nhập vào một ký tự bất kỳ")
ch = input() # 'a', 4

## kiểm tra điều kiện
if ch >= '0' and ch <= '9':
    print(f"{ch} is a digit")
else:
    print(f"{ch} is not a digit")
