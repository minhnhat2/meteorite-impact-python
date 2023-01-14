import pygame
import random

width=800
height=600
#khởi tạo
pygame.init()
#tạo màn hình
screen= pygame.display.set_mode((width,height))
#tạo nhân vật người chơi
player=pygame.Rect(width/2,height/2,20,20) #tạo một đối tượng người chơi có chiều rộng là 20 và chiều cao là 20, đồng thời đặt đối tượng đó ở giữa màn hình.
#tiểu hành tinh
asteroids=[]
for i in range (10):
    x=random.randint(0,width)        ###tạo ra 10 đối tượng tiểu hành tinh, mỗi đối tượng có vị trí x và y ngẫu nhiên trong màn hình, chiều rộng và chiều cao là 50.
    y=random.randint(0,height)
    asteroids.append(pygame.Rect(x,y,50,50))
#nét chữ
font=pygame.font.Font(None,30)
#clock
clock=pygame.time.Clock() #tạo đối tượng đồng hồ để kiểm soát tốc độ khung hình của trò chơi.
#score
score=0
# vòng lặp trò chơi
while True:  #vòng lặp trò chơi chính chạy cho đến khi người dùng đóng trò chơi.
    #xử lý sự kiện
    for event in pygame.event.get():  #xử lý mọi sự kiện, chẳng hạn như người dùng đóng trò chơi.
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    #cập nhập nút di chuyển
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x-=5
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x+=5
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y-=5
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y+=5
    #cập nhật vị trí người chơi
    player.clamp_ip(pygame.Rect(0,0,width,height)) #đảm bảo rằng trình phát nằm trong ranh giới màn hình.
    #cập nhật vị trí của từng tiểu hành tinh và nếu một tiểu hành tinh biến mất khỏi màn hình, 
    #nó sẽ được định vị lại ở đầu màn hình với vị trí x ngẫu nhiên.
    for asteroid in asteroids:
        asteroid.y+=5
        if asteroid.y>height:
            asteroid.y=0
            asteroid.x=random.randint(0,width)
        #kiểm tra va chạm
        #kiểm tra va chạm giữa người chơi và từng tiểu hành tinh và nếu va chạm xảy ra, 
        #điểm sẽ tăng lên và tiểu hành tinh được định vị lại ở đầu màn hình với vị trí x ngẫu nhiên.
        for asteroid in asteroids:
            if player.colliderect(asteroid):
                score+=1
                asteroid.x=random.randint(0,width)
                asteroid.y=0
    #vẽ đồ vật
    screen.fill((0,0,0)) #lấp đầy màn hình bằng một màu đen.
    for asteroid in asteroids: #vẽ từng tiểu hành tinh trên màn hình.
        pygame.draw.rect(screen,(255,255,255),asteroid)
    pygame.draw.rect(screen, (255,0,0), player) #vẽ người chơi trên màn hình.
    #vẽ score
    text=font.render(f"Score: {score}",True,(255,255,255)) #tạo một đối tượng văn bản hiển thị điểm hiện tại bằng màu trắng.
    screen.blit(text, (10,10)) #vẽ đối tượng văn bản trên màn hình tại vị trí (10,10).
    #cập nhật màn hình
    pygame.display.flip() #cập nhật màn hình để hiển thị trình phát, tiểu hành tinh và điểm số.
    #tick the clock
    clock.tick(60) #kiểm soát tốc độ khung hình của trò chơi, với 60 khung hình mỗi giây.
