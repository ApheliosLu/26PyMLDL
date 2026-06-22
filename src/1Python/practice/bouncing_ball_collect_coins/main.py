# Author: ApheliosLu
# 2026-06-22 19:47:55
# https://github.com/ApheliosLu

import pygame
import random
import sys

# 初始化pygame
pygame.init()

# 窗口设置
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("弹跳小球收集金币")

# 颜色定义
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GOLD = (255, 215, 0)
BLACK = (0, 0, 0)

# 玩家小球设置
player_size = 30
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# 金币设置
coin_size = 20
coin_x = random.randint(0, WIDTH - coin_size)
coin_y = random.randint(0, HEIGHT - coin_size)

# 分数
score = 0
font = pygame.font.Font(None, 36)

# 游戏主循环
clock = pygame.time.Clock()
running = True

while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 键盘控制移动
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # 碰撞检测：玩家吃到金币
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size, coin_size)
    if player_rect.colliderect(coin_rect):
        score += 1
        # 生成新金币
        coin_x = random.randint(0, WIDTH - coin_size)
        coin_y = random.randint(0, HEIGHT - coin_size)

    # 绘制画面
    screen.fill(BLACK)
    pygame.draw.circle(
        screen,
        BLUE,
        (player_x + player_size // 2, player_y + player_size // 2),
        player_size // 2,
    )
    pygame.draw.circle(
        screen, GOLD, (coin_x + coin_size // 2, coin_y + coin_size // 2), coin_size // 2
    )

    # 显示分数
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # 更新显示
    pygame.display.flip()
    clock.tick(60)  # 限制帧率为60FPS

# 退出游戏
pygame.quit()
sys.exit()
