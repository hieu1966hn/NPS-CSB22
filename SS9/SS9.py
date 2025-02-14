## Buổi 8: Hàm, module

### Khởi tạo 1 hàm 
def sum(n, m):
    return n + m
    # print(n + m)

## Gọi hàm sum
tong = sum(3, 6) # 9
# print(tong) ## print(sum(3, 6))

## Viết hàm kiểm tra chẵn lẻ
def kiem_tra_chan_le(n):
    ## kiểm tra đây có phải là "số hay không"
    if str(n).isdigit(): # là số rồi
        if n % 2 == 0:
            return "even"
        else:
            return 'odd'
    else:
        return False
    
print(kiem_tra_chan_le(3))