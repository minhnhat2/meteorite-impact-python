import pygame
import random

width=800
height=600
#khởi tạo
pygame.init()
#tạo màn hình
screen= pygame.display.set_mode((width,height))
#tạo nhân vật người chơi
player=pygame.Rect(width/2,height/2,20,20) 
asteroids=[] 
for i in range (10):
    x=random.randint(0,width)     
    y=random.randint(0,height)
    asteroids.append(pygame.Rect(x,y,50,50))
#nét chữ
font=pygame.font.Font(None,30)
#clock
clock=pygame.time.Clock()
#score
score=0
# vòng lặp trò chơi
while True:  
    #xử lý sự kiện
    for event in pygame.event.get(): 
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
    player.clamp_ip(pygame.Rect(0,0,width,height)) 
    #cập nhật vị trí của từng tiểu hành tinh và nếu một tiểu hành tinh biến mất khỏi màn hình, 
    #nó sẽ được định vị lại ở đầu màn hình với vị trí x ngẫu nhiên.
    for asteroid in asteroids:
        asteroid.y+=5
        if asteroid.y>height:
            asteroid.y=0
            asteroid.x=random.randint(0,width)
 
        for asteroid in asteroids:
            if player.colliderect(asteroid):
                score+=1
                asteroid.x=random.randint(0,width)
                asteroid.y=0
    #vẽ đồ vật
    screen.fill((0,0,0)) 
    for asteroid in asteroids: ]
        pygame.draw.rect(screen,(255,255,255),asteroid)
    pygame.draw.rect(screen, (255,0,0), player) ]
    #vẽ score
    text=font.render(f"Score: {score}",True,(255,255,255)) 
    screen.blit(text, (10,10))
    #cập nhật màn hình
    pygame.display.flip() 
    #tick the clock
    clock.tick(60) 
