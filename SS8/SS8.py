## Viết hàm in ra số người dùng nhập vào

# Định nghĩa hàm
# def print_number(n): ## n: tham số đầu vào (biến số)
#     print(n)
    
# ## Gọi hàm
# print_number(5) ## 5: đối số đầu vào (argument)


## Bài 1: Xây dựng hàm tính giá trị tuyệt đối của một số nguyên
## Bài 2: Xây dựng hàm tính diện tích/Chu vi hình tròn dựa vào bán kính truyền vào

## Bài 3: Xây dựng hàm kiểm tra một số nguyên có phải là số chẵn hay không

def is_even(n):
    if n % 2 == 0: ## n là số chẵn
        return True
    else:
        return False

# print(is_even(4)) ## False
    
    
## Bài 4: Xây dựng hàm kiểm tra một số nguyên có phải là số nguyên tố hay không
## Số nguyên tố: là số lớn hơn 1 và chỉ chia hết cho 1 và chính nó
def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, n):
        print(i)
        if n % i == 0:
            return False
    return True

# print(is_prime(3)) ## True


## Gọi hàm kiểm tra số lớn hơn:
import SS8_def

# print(SS8_def.max_number(1, 2))

# print(SS8_def.leap_year(2000))

arr = [1, 2, 100, -3, "hi", 123, 'hello']
print(SS8_def.sum_list(arr))