# for i in range(1, 101):
#     print(i, end=" ")


## Bài toán nhập vào số dương và in ra nó. Nếu n < 0 => yêu cầu nhập lại
# print("Mời người dùng nhập n: ")
# n = float(input())
# while n<=0:
#     print("Mời người dùng nhập n: ")
#     n = float(input())
# print(f"{n} là một số dương!")



### Ví dụ với break
# for i in range(10):
#     if i == 5:
#         break
#     print(i, end=" ")
    
    
### ví dụ với continue
# for i in range(10):
#     if i == 5:
#         continue
#     print(i, end=" ")


### Bài thực hành 1:
# print("Input number: ", end="")
# num = int(input()) # 5

# vế 1
# line = "#"
# for i in range(num):
#     print(line)
#     line = line + "#"
    
    
    
    
    
### Đề bài thực hành số 3: 
print('Input number: ', end="")
num = int(input()) # 3! = 1*2*3

## kiểm tra điều kiện
if num < 0:
    print("Invalid")
else:
    fact = 1
    for i in range(2, num + 1):
        fact = fact * i # 2*3 = 6
    print(f'{num}! = {fact}')
        
        