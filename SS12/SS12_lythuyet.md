Buổi 12: Xử lý Files
- File Path: Dùng để truy cập vào một file ở trong OS
Gồm 3 phần: 
+ folder path: Vị trí của folder chứa file. thứ tự các folder được chia cắt bởi dấu / (UNIX) hoặc \ (Window)
+ file name: Tên file
+ Extension: định dạng của file, bắt đầu bằng dấu.


Phân loại file: Khi xử lý, ta có t hể chia file thành 2 loại:
1. TEXT FILE: Chứa dữ liệu dạng chữ. Không bao gồm định dạng như: màu sắc, kiểu chữ, ... (Ta chỉ quan tâm đến xử lý trên text file)

exp: txt, csv, hmtl, css...


2. BINARY FILE: Các loại file khác, mỗi file có cách xử lý khác nhau tùy vào định dạng.

exp: jpg, png, doc, xls, rar/zip, ....


FILE PATH: 
+ Đường dẫn tuyệt đối: Bắt đầu từ thư mục gốc
VD: C:\Users\ADMIN\Desktop\sample.txt  (window)
+ Đường dẫn tương đối: Không chứa thư mục gốc. Khi chạy code, chương trình mặc định bắt đầu từ vị trí hiện tại của trình thực thi.
VD: SS12/SS12.py


XỬ LÝ FILE
- Tạo file
- Open File
- Read File
- Write File
- Delete File