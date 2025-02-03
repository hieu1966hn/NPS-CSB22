### Chỉ viết hàm ở đây, gọi hàm ở file khác

## 1. Viết hàm tìm số lớn hơn trong 2 số truyền vào
## 2. Viết hàm kiểm tra năm đó có phải là năm nhuận hay không?
## 3. Viết hàm tính tổng một List cho trước. Nếu như Array tồn tại phần tử 
# không phải là số => bỏ qua phần tử đó.

def max_number(a, b):
    if a > b:
        return a
    elif a == b:
        return "không có số lớn hơn"
    else:
        return b
    
def leap_year(y): 
    if y % 4 == 0 and y % 100 != 0:
        return True
    elif y % 400 == 0:
        return True
    else:
        return False
    
    



def sum_list(arr):
    sum = 0
    for i in arr:
        if str(i).isdigit(): ## True
            sum = sum + i
        else: 
            continue
    return sum
        