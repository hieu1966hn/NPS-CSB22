Bài 3: Kiểu dữ liệu Boolean và Cấu trúc điều kiện
- Giới thiệu về KDL Boolean
- Các phép toán trên Boolean
- Cách sử dụng câu lệnh điều kiện


KDL Boolean
- Trong Python, KDL Boolean chỉ bao gồm 2 giá trị là True và False
+ Các giá trị boolean thường thể hiện tính đúng hoặc sai của một mệnh đề nào đó. Ví dụ: 
phép so sánh 1 < 2 có kết quả là True
phép so sánh 1 > 2 có kết quả là False

Tên nhà toán học & logic học người Anh: George Boole

1. Phép toán so sánh: >, <, >=, <=, ==, !=
- Cho phép ta kiểm tra quan hệ trước sau giữa hai giá trị bất kỳ. Kết quả của một phép so sánh trong Python là một giá trị boolean.

2. Phép toán logic (and, or, not)
- Cho phép ta kết hợp các giá trị boolean trong một biểu thức logic. Kết quả của một phép logic trong Python là một giá trị boolean.
+ and: phép toán logic tìm "False": trong các biểu thức, nếu tồn tại 1 biểu thức có kết quả là "False" => output: False. Ngược lại, output: True.
+ or: phép toán logic tìm "True": trong các biểu thức, nếu tồn tại 1 biểu thức có kết quả là "True" => output: True. Ngược lại, output: False.
+ not: Ngược lại với biểu thức đang xét. VD not False => True

3. Cấu trúc điều kiện
- Cho phép ta quyết định hành động nào được thực hiện, dựa trên các điều kiện cho trước.
Exp: Người dùng được truy cập vào tài khoản với điều kiện là tên đăng nhập và mật khẩu được nhập đúng.
- Trong Python, cấu trúc điều kiện được thể hiện bằng từ khóa: if, else, elif



Đề bài thực hành: 

Bài 1: Chẵn lẻ: Yêu cầu người dùng nhập vào 1 số nguyên. Hãy kiểm tra tính chẵn lẻ của số nguyên đó.
input: 4
output: 4 is even

Bài 2: Nhập vào 1 số thực. Kiểm tra số thực đó có phải là số nguyên hay không. 
input: 3
output: 3 is an interger

Bài 3: Nhập vào một ký tự. Kiểm tra ký tự đó có phải là một chữ số hay không.
Ví dụ 1:
input: 3
ouput: '3' is a digit

Ví dụ 2:
input: m
ouput: 'm' is not a digit








