Buổi 8: Hàm và Module
- Cách viết hàm và mục đích sử dụng hàm
- Phân biệt được hàm print và hàm return
- Cách viết hàm thành module và import module


Hàm: là một đoạn code (chương trình con) dùng để thực hiện một việc nào đó. Có hai loại hàm:
- Hàm built-in: Hàm có sẵn trong python: input(), print(),...
- Hàm do người dùng viết

Cách viết hàm:
def <ten_ham> ():
    statement ....


Phạm vi biến số: 
- Global: Là biến được tạo ngoài hàm, được duy trì trong toàn bộ chương trình code
- Local: là biến được tạo trong hàm. Có tác dụng trong hàm đó và biến mất sau khi hàm kết thúc.
** Trong trường hợp biến local và global có cùng tên => sẽ ưu tiên biến Local trước.


Module: 
- Tách hàm ra file để có thể sử dụng ở nhiều chương trình khác nhau.
- File hàm phải ở cùng folder với chương trình
- Cú pháp import