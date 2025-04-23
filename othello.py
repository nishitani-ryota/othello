import pygame
import sys

#クリックしたマスを指定する関数
def makecircle(x,y):
    if x < 100 and y % 100 != 0:
        x = 50
        z = y // 100
        y = z *100 +  50
        return x,y
    if x < 200 and y % 100 != 0:
        x = 150
        z = y // 100
        y = z *100 +  50
        return x,y
    if x < 300 and y % 100 != 0:
        x = 250
        z = y // 100
        y = z *100 +  50
        return x,y
    if x < 400 and y % 100 != 0:
        x = 350
        z = y // 100
        y = z *100 +  50
        return x,y
    if x < 500 and y % 100 != 0:
        x = 450
        z = y // 100
        y = z *100 +  50
        return x,y
    if x < 600 and y % 100 != 0:
        x = 550
        z = y // 100
        y = z *100 +  50
        return x,y
    if x < 700 and y % 100 != 0:
        x = 650
        z = y // 100
        y = z *100 +  50
        return x,y
    if x < 800 and y % 100 != 0:
        x = 750
        z = y // 100
        y = z *100 +  50
        return x,y
    
def yellow(num,yellow_a,yellow_b):
    for a in board:
        for b in board:
            if board_dict[(a, b)] == num:
                for c in tateyokonaname:
                    serch = True
                    current_a = a
                    current_b = b
                    while serch:
                        if current_a + c[0] > 0 and current_b + c[1] > 0 and current_a + c[0] < 850 and current_b + c[1] < 850 and screen.get_at((current_a + c[0], current_b + c[1])) == yellow_a and screen.get_at((current_a, current_b)) == yellow_b:
                            serchlist.append((current_a + c[0], current_b + c[1]))
                            current_a += c[0]
                            current_b += c[1]
                            if current_a > 0 and current_b > 0 and current_a < 850 and current_b < 850 and current_a + c[0]> 0 and current_b + c[1] > 0 and current_a + c[0] < 850 and current_b + c[1] < 850 and board_dict[(current_a + c[0],current_b + c[1])] == 0:
                                list.append((current_a + c[0], current_b + c[1]))
                        else:
                            serch = False

def reverse_serch(serch_1,serch_2):
    serch = True
    current_x = x
    current_y = y
    reverse = []
    while serch:
        if current_x + c[0] > 0 and current_y + c[1] > 0 and current_x + c[0] < 850 and current_y + c[1] < 850 and current_x + c[0] > 0 and current_y + c[1] > 0 and current_x + c[0] < 850 and current_y + c[1] < 850 and screen.get_at((current_x + c[0], current_y + c[1])) ==serch_1 :
            reverse.append((current_x + c[0], current_y + c[1]))
            current_x += c[0]
            current_y += c[1]
            if current_x + c[0] > 0 and current_y + c[1] > 0 and current_x + c[0] < 850 and current_y + c[1] < 850 and current_x + c[0] > 0 and current_y + c[1] > 0 and current_x + c[0] < 850 and current_y + c[1] < 850 and screen.get_at((current_x + c[0], current_y + c[1])) ==serch_2 :
                true_reverse.extend(reverse)
                serch = False 
            elif current_x + c[0] > 0 and current_y + c[1] > 0 and current_x + c[0] < 850 and current_y + c[1] < 850 and current_x + c[0] > 0 and current_y + c[1] > 0 and current_x + c[0] < 850 and current_y + c[1] < 850 and board_dict[(current_x + c[0], current_y + c[1])] == 0: 
                reverse = []
                serch = False
        else:
            serch = False                                        
pygame.init()

screen = pygame.display.set_mode((800,800))
screen.fill((0,100,0))
board = [50,150,250,350,450,550,650,750]
board_dict = {}
for a in board:
    for b in board:
        board_dict[(a,b)] = 0
pygame.draw.circle(screen,(255,255,255),(350,350),50)
board_dict[(350,350)] = 1
pygame.draw.circle(screen,(255,255,255),(450,450),50)
board_dict[(450,450)] = 1
pygame.draw.circle(screen,(0,0,0),(450,350),50)
board_dict[(450,350)] = 2
pygame.draw.circle(screen,(0,0,0),(350,450),50)
board_dict[(350,450)] = 2
pygame.display.flip()
player =1
running = True
tateyokonaname = [(0,100),(0,-100),(100,0),(-100,0),(100,100),(100,-100),(-100,-100),(-100,100)]
font = pygame.font.Font(None, 36)

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        draw = True
        while draw:        
            #最初のプレイヤーがクリックした箇所を白くする
            if player ==1:
                list = []
                serchlist = []
                end_white = []
                end_black = []
                yellow(1,(0, 0, 0),(255, 255, 255))
                
                for d in list:
                    if board_dict[(d)] == 0:
                        pygame.draw.circle(screen, (255, 255, 0), (d), 50)
                        pygame.draw.circle(screen, (0,100,0), (d), 45) 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos
                    (x,y) = makecircle(x,y)
                    player -= 1 
                    pygame.draw.circle(screen,(255,255,255),(x,y),50)
                    board_dict[(x, y)] = 1
                    true_reverse = []
                    
                    for c in tateyokonaname:
                        reverse_serch((0, 0, 0),(255, 255, 255))
                        
                    for b in true_reverse:
                        pygame.draw.circle(screen, (255, 255, 255), (b), 50)
                        board_dict[(b)] = 1

                    for d in list:
                        if board_dict[(d)] == 0:
                            pygame.draw.circle(screen, (0,100,0), (d), 50)
                    
                    for a in board:
                            skip = False
                            for b in board:
                                if board_dict[(a,b)] == 0:
                                    skip = True
                                elif a==750 and b == 750 and board_dict[(750,750)] != 0:
                                    for a in board:
                                        for b in board:
                                            if board_dict[(a,b)] == 1:
                                                end_white.append((a,b))
                                            elif board_dict[(a,b)] == 2:
                                                end_black.append((a,b))
                                        
                                    screen.fill((0, 0, 0))  # 背景を黒に塗りつぶす
                                    if len(end_white) > len(end_black):
                                        text = font.render("white win", True, (255, 255, 255))
                                        text_rect = text.get_rect(center=(400, 400))
                                        screen.blit(text, text_rect)
                                    elif len(end_white) < len(end_black):
                                        text = font.render("black win", True, (255, 255, 255))
                                        text_rect = text.get_rect(center=(400, 400))
                                        screen.blit(text, text_rect)
                                    else:
                                        text = font.render("draw", True, (255, 255, 255))
                                        text_rect = text.get_rect(center=(400, 400))
                                        screen.blit(text, text_rect)
                                    pygame.display.flip()  # 画面更新
                            if skip:
                                break

            elif player == 0 :
                    list = []
                    serchlist = []
                    end_white = []
                    end_black = []
                    yellow(2,(255, 255, 255),(0, 0, 0))
                    
                    for d in list:
                        if board_dict[(d)] == 0:
                            pygame.draw.circle(screen, (255, 255, 0), (d), 50)
                            pygame.draw.circle(screen, (0,100,0), (d), 45) 
                    if event.type == pygame.MOUSEBUTTONDOWN:   
                        (x,y) = event.pos
                        (x,y) = makecircle(x,y) 
                        player += 1
                        pygame.draw.circle(screen,(0,0,0),(x,y),50)
                        board_dict[(x, y)] = 2
                        true_reverse = []
                        
                        for c in tateyokonaname:
                            reverse_serch((255, 255, 255),(0, 0, 0))
                            
                        for b in true_reverse:
                            pygame.draw.circle(screen, (0,0,0), (b), 50)
                            board_dict[(b)] = 2
                        for d in list:
                            if board_dict[(d)] == 0:
                                pygame.draw.circle(screen, (0,100,0), (d), 50)
                                
                        for a in board:
                            skip = False
                            for b in board:
                                if board_dict[(a,b)] == 0:
                                    skip = True
                                elif a==750 and b == 750 and board_dict[(750,750)] != 0:
                                    for a in board:
                                        for b in board:
                                            if board_dict[(a,b)] == 1:
                                                end_white.append((a,b))
                                            elif board_dict[(a,b)] == 2:
                                                end_black.append((a,b))
                                        
                                    screen.fill((0, 0, 0))  # 背景を黒に塗りつぶす
                                    if len(end_white) > len(end_black):
                                        text = font.render("white win", True, (255, 255, 255))
                                        text_rect = text.get_rect(center=(400, 400))
                                        screen.blit(text, text_rect)
                                    elif len(end_white) < len(end_black):
                                        text = font.render("black win", True, (255, 255, 255))
                                        text_rect = text.get_rect(center=(400, 400))
                                        screen.blit(text, text_rect)
                                    else:
                                        text = font.render("draw", True, (255, 255, 255))
                                        text_rect = text.get_rect(center=(400, 400))
                                        screen.blit(text, text_rect)
                                    pygame.display.flip()  # 画面更新
                            if skip:
                                break
            draw = False                   
        pygame.display.flip()

    #pygame.time.Clock().tick(60)
#ゲーム終了
pygame.quit()
sys.exit()
