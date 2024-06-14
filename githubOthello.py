import pygame
pygame.init()

#関数------------------------------------------------------------------------------------------------------
#石を置ける場所の取得

#グリッド線
def draw_grid():
    if screen:
        for i in range(square_num):
            #横線
            pygame.draw.line(screen,BLACK,(0,i*square_size),(screen_width,i*square_size),3)
            #縦線
            pygame.draw.line(screen,BLACK,(i*square_size,0),(i*square_size,screen_height),3)

#石の描画
def draw_board():
    for row_index,row in enumerate(board):
        for col_index,col in enumerate(row):
            if col == 1:
                pygame.draw.circle(screen,BLACK,(col_index * square_size + 50, row_index * square_size + 50),45)
            elif col == -1:
                pygame.draw.circle(screen,WHITE,(col_index * square_size + 50, row_index * square_size + 50),45)
#石を置ける場所の取得
def get_validation_potitions():
    valid_position_list = []
    for row in range(square_num):
        for col in range(square_num):
            #石を置いていないマスのみチェック
            if board[row][col] == 0:
                for vx,vy in vec_table:
                    x = vx + col
                    y = vy +row
                    #マスの範囲内、かつプレイやーの石と異なる意思がある場合、その方向は引き続きチェック
                    if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == -player:
                            while True:
                                x += vx
                                y += vy
                                #プレイヤーの石と異なる石がある場合、その方向はひきつづきチェック
                                if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == -player:
                                    continue
                                #プレイヤーの石と同色の石がある場合、石を置けるためのインデックスを保存
                                elif 0 <= x < square_num and 0 <= y < square_num and board[y][x] == player:
                                    valid_position_list.append((col,row))
                                    break
                                else:
                                    break
    return valid_position_list
#石をひっくり返す
def flip_pieces(col,row):
    for vx,vy in vec_table:
        flip_list = []
        x = vx + col
        y = vy + row
        while 0 <= x < square_num and 0 <= y < square_num and board[y][x] == -player:
                flip_list.append((x,y))
                x += vx
                y += vy
                if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == player:
                    for flip_x, flip_y in flip_list:
                        board[flip_y][flip_x] = player
#--------------------------------------------------------------------------------------------------------------------
#ウィンドウ作成
width = 100
screen_width = 800
screen_height = 800 
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("オセロ")
#マスの設定
square_num = 8
square_size = screen_width // square_num
#fps設定
FPS = 60
clock = pygame.time.Clock()
#色の設定
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
#盤面(黒:1,白:-1)
board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,-1,1,0,0,0],
        [0,0,0,1,-1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
#プレイヤー
player = 1
vec_table = [
    (-1,-1),    #左上
    (0,-1),     #上
    (1,-1),     #右上
    (-1,0),     #左
    (1,0),      #右
    (-1,1),     #左下
    (0,1),      #下
    (1,1) ]     #右下
game_over = False
pass_num = 0
#表示文の設定
font = pygame.font.SysFont(None, 100, bold=False, italic=False)
black_win_surface = font.render("Black Win!", False, BLACK, RED)
white_win_surface = font.render("White Win!", False, WHITE, RED)
draw_surface = font.render("Draw...", False, BLUE, RED)
reset_surface = font.render("Click to reset!", False, BLACK, RED)
startt = font.render("start", False, BLACK, GREEN)
exitt = font.render("exit", False, BLACK, RED)
#マウスクリックでstart-----------------------------------------------------------------------------------------------------------------------------
start = True
while start:
    rect = pygame.Rect(300, 300, 152, 68)
    #screen.fill((255,255,255), rect)
    screen.blit(startt,(300,300))
    for starts in pygame.event.get():
        #右上の×押したら画面閉じる
        if starts.type == pygame.QUIT:
            pygame.quit()
        if starts.type == pygame.KEYDOWN:
            #ESCAPE押したら画面閉じる
            if starts.key == pygame.K_ESCAPE:
                pygame.quit()
        if starts.type == pygame.MOUSEBUTTONDOWN:
            mx,my = pygame.mouse.get_pos()
            #rect = pygame.Rect(300, 300, 600, 600)
            #クリックした箇所がrectの範囲内であればif文実行
            if rect.collidepoint(mx, my):
                run = True
                start = False
    pygame.display.update()
    clock.tick(FPS)
#-----------------------------------------------------------------------------------------------------------------------------
#メインループ##########################################################################################
run = True
fullscreen = False
while run:
    #背景の塗りつぶし
    screen.fill(GREEN)
    draw_grid()
    if fullscreen ==False:
    #石の絵画
        draw_board()
    #石を置ける場所の取得
        valid_position_list = get_validation_potitions()
    #valid_position_list = get_validation_potitions()で取得した場所に石の置ける場所を描画
        for x,y in valid_position_list:
            pygame.draw.circle(screen,YELLOW,(x * square_size + 50, y * square_size + 50),45,3)
    #石を置ける場所がない場合、パス
    if len(valid_position_list) < 1:
        player *= -1
        pass_num += 1
    #ゲームオーバー判定
    if pass_num > 1:
        pass_num = 2
        game_over = True
    #勝敗チェック
    black_num = 0
    white_num = 0
    if game_over:
        black_num = sum(row.count(1) for row in board)
        white_num = sum(row.count(-1) for row in board)
        if black_num > white_num:
            screen.blit(black_win_surface,(230,200))
        elif black_num < white_num:
            screen.blit(white_win_surface,(230,200))
        else:
            screen.blit(draw_surface,(230,200))
            screen.blit(reset_surface, (180,400))
    #イベントの取得     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            #ウインドウモード
            if event.key == pygame.K_c:
                pygame.display.set_mode((800, 800))
                fullscreen = False
            #フルスクリーン
            if event.key == pygame.K_f:
                full = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                fullscreen = True
                run = False
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
        #マウスクリック
        if fullscreen == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over == False:
                    mx,my = pygame.mouse.get_pos()
                    if fullscreen == False:
                        x = mx // square_size
                        y = my // square_size
                    
                        if board [y][x] == 0 and (x,y) in valid_position_list:
                            #石をひっくり返す
                            flip_pieces(x,y)
                            board[y][x] = player
                            player *= -1
                            pass_num = 0
                else:
                    board = [
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,-1,1,0,0,0],
                        [0,0,0,1,-1,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0],
                        [0,0,0,0,0,0,0,0]]
                    player = 1
                    game_over = False
                    pass_num = 0 
    #更新
    pygame.display.update()
    clock.tick(FPS)
##################################################################################################

screen_width = 800
full = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
square_num = 8
square_size = screen_width // square_num
#fps設定
FPS = 60
clock = pygame.time.Clock()
#盤面(黒:1,白:-1)

player = 1
vec_table = [
    (-1,-1),    #左上
    (0,-1),     #上
    (1,-1),     #右上
    (-1,0),     #左
    (1,0),      #右
    (-1,1),     #左下
    (0,1),      #下
    (1,1) ]     #右下
game_over = False
pass_num = 0
board = [
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,-1,1,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,1,-1,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2]]
#色の設定
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
#表示文の設定
font = pygame.font.SysFont(None, 100, bold=False, italic=False)

#関数-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#石を置ける場所の取得
def full_potitions():
    full_list = []
    for row in range(square_num):
        for col in range(4,12):
            #石を置いていないマスのみチェック
            if board[row][col] == 0:
                
                for vx,vy in vec_table:
                    x = vx + col
                    y = vy +row
                    #マスの範囲内、かつプレイやーの石と異なる意思がある場合、その方向は引き続きチェック
                    if 4 <= x < 12 and 0 <= y < 8 and board[y][x] == -player:
                            while True:
                                x += vx
                                y += vy
                                #プレイヤーの石と異なる石がある場合、その方向はひきつづきチェック
                                if 4 <= x < 12 and 0 <= y < 8 and board[y][x] == -player:
                                    continue
                                #プレイヤーの石と同色の石がある場合、石を置けるためのインデックスを保存
                                elif 4 <= x < 12 and 0 <= y < 8 and board[y][x] == player:
                                    full_list.append((col,row))
                                    break
                                else:
                                    break
    return full_list
#石をひっくり返す
def full_pieces(col,row):
    for vx,vy in vec_table:
        flip_list = []
        x = vx + col
        y = vy + row
        while 4 <= x < 12 and 0 <= y < 8 and board[y][x] == -player:
            flip_list.append((x,y))
            x += vx
            y += vy
            if 4 <= x < 12 and 0 <= y < 8 and board[y][x] == player:
                for flip_x, flip_y in flip_list:
                    board[flip_y][flip_x] = player
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#フルスクリーン時メイン#############################################################################################################################################################################

while fullscreen:
    #背景の塗りつぶし
    full.fill(GREEN)
    #石を置ける場所の取得
    full_list = full_potitions()
    #クリックする範囲
    rect = pygame.Rect(1400, 0, 127, 68)
    screen.fill((255,255,255), rect)
    #startを表示させる範囲
    screen.blit(exitt,(1400,0))
    #イベントの取得     
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.display.set_mode((800,800))
                pygame.quit()
        #マウスクリック
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_over == False:
                mx,my = pygame.mouse.get_pos()
                #クリックした箇所がrectの範囲内であればif文実行
                if rect.collidepoint(mx, my):
                    pygame.quit()
                x = mx // 100
                if 50 <= my < 100: #0
                    y = my // 100 
                if 100 <= my < 150: #0
                    y = my // 100 -1
                if 150 <= my < 200: #1
                    y = my // 100 
                if 200 <= my < 250: #1
                    y = my // 100 -1
                if 250 <= my < 300: #2
                    y = my // 100 
                if 300 <= my < 350: #2
                    y = my // 100 -1
                if 350 <= my < 400:#3
                    y = my // 100
                if 400 <= my < 450: #3
                    y = my // 100 -1
                if 450 <= my < 500: #4
                    y = my // 100
                if 500 <= my < 550: #4
                    y = my // 100 -1 
                if 550 <= my < 600: #5
                    y = my // 100
                if 600 <= my < 650: #5
                    y = my // 100 - 1
                if 650 <= my < 700: #6
                    y = my // 100
                if 700 <= my < 750: #6
                    y = my // 100 - 1
                if 750 <= my <= 800: #7
                    y = my // 100
                if 800 <= my <= 850: #7
                    y = my // 100 - 1
                if board[y][x] == 0 and (x,y) in full_list:
                    #石をひっくり返す
                    full_pieces(x,y)
                    board[y][x] = player
                    player *= -1
                    pass_num = 0
            else:
                    board = [
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,-1,1,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,1,-1,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2]]
                    player = 1
                    game_over = False
                    pass_num = 0    
    #colが1だったら黒石を置いて-1だったら白石を置く設定
    for row_index,row in enumerate(board):
        for col_index,col in enumerate(row):
            if col == 1:
                pygame.draw.circle(full,BLACK,(col_index * square_size + 50, row_index * square_size + 100),45)
            elif col == -1:
                pygame.draw.circle(full,WHITE,(col_index * square_size + 50, row_index * square_size + 100),45)
    for i in range(square_num+1):
        for line in range(4):
            pygame.draw.line(full,GREEN,(0,line*square_size),(398,line*square_size),3)
            pygame.draw.line(full,GREEN,(line*square_size,0),(line*square_size,800),3)
        for line in range(4,9):
            pygame.draw.line(full,GREEN,(0,line*square_size),(398,line*square_size),3)
            pygame.draw.line(full,GREEN,(line*square_size,0),(line*square_size,48),3)
            pygame.draw.line(full,BLACK,(400,i*square_size+50),(1200,i*square_size+50),3)
            pygame.draw.line(full,BLACK,((i+4)*square_size,50),((i+4)*square_size,850),3)
            #石を置ける場所の取得
    full_list = full_potitions()
    #石を置ける場所を黄色の円で表示
    for x,y in full_list:
        pygame.draw.circle(full,YELLOW,(x * square_size + 50, y * square_size + 100),45,3)
    #石を置ける場所がない場合、パス
    if len(full_list) < 1:
        player *= -1
        pass_num += 1
    #ゲームオーバー判定
    if pass_num > 1:
        pass_num = 2
        game_over = True
    #勝敗チェック
    black_num = 0
    white_num = 0
    if game_over:
        black_num = sum(row.count(1) for row in board)
        white_num = sum(row.count(-1) for row in board)
        if black_num > white_num:
            screen.blit(black_win_surface,(630,315))
        elif black_num < white_num:
            screen.blit(white_win_surface,(630,315))
        else:
            screen.blit(draw_surface,(630,315))
        screen.blit(reset_surface, (575,500))
    #更新
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()