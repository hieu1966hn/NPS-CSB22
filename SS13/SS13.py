import pygame

## Khởi tạo các module cần thiết của pygame bằng hàm init.
pygame.init()

####: Sử dụng pygame để vẽ và hiển thị một hình chữ nhật đơn giản
screen = pygame.display.set_mode((800, 600))

## Đặt tên cho cửa sổ game: 
pygame.display.set_caption("Vẽ hình chữ nhật với Pygame")

#### Định nghĩa màu sắc (R, G, B)
white = (255, 255, 255)
red = (255 , 0, 0)

### Vẽ một hình chữ nhật màu đỏ
hcn = pygame.Rect(200, 200, 200, 150)
pygame.draw.rect(screen, red, hcn)

#### Cập nhật màn hình để hiển thị hình chữ nhật
pygame.display.flip()

#### Đợi người dùng thoát ra khỏi cửa sổ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
### thoát pygame
pygame.quit()




