Buổi 13: Tìm hiểu về thư viện Pygame
- Làm quen với thư viện Pygame
- import pygame
- Cách vẽ các khối: Hàm Rect()
- Hàm display()

Thư viện: pygame là bộ thư viện sử dụng để phát triển trò chơi trong Python. Nó cung cấp các chức năng để làm việc với: đồ họa, âm thanh và các yếu tố khác của một trò chơi.

# Để vẽ các khối, chúng ta cần cửa sổ để hiển thị chúng

# Tạo cửa sổ bằng hàm: display.set_mode():
screen = pygame.display.set_mode((width, height))

# Vẽ các khối với hàm: draw.rect() || x, y là tọa độ góc bên trên trái của hình chữ nhật.
rect = pygame.Rect(x, y, width, height)


# Để hiển thị những gì vừa vẽ, chúng ta cần cập nhật màn hình bằng hàm: 
display.flip() hoặc dipslay.update()

# import sys
Là module cung cấp các hàm và biến để tương tác với hệ thống Python.