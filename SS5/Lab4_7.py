### Chữa bài lab số 7
from turtle import *

## thiết lập hình dạng của con trỏ vẽ thành con rùa (turtle).
shape('turtle')

# Khởi tạo giá trị bán kính ban đầu: 1
r = 1

## Vòng lặp lặp lại 20 lần. Mỗi lần lặp sẽ thực hiện các thao tác vẽ một cung tròn nửa đường tròn bán kính thay đổi
for i in range(20):
    circle(r, 180)
    r = r + 10

mainloop()

