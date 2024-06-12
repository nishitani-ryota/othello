import pygame
pygame.init()

#関数------------------------------------------------------------------------------------------------------
#石を置ける場所の取得
def full_potitions():
    full_list = []
    for row in range(square_num):
        for col in range(4,12):
            #石を置いていないマスのみチェック
            if boards[row][col] == 0:
                
                for vx,vy in vec_table:
                    x = vx + col
                    y = vy +row
                    #マスの範囲内、かつプレイやーの石と異なる意思がある場合、その方向は引き続きチェック
                    if 4 <= x < 12 and 0 <= y < 8 and boards[y][x] == -player:
                            while True:
                                x += vx
                                y += vy
                                #プレイヤーの石と異なる石がある場合、その方向はひきつづきチェック
                                if 4 <= x < 12 and 0 <= y < 8 and boards[y][x] == -player:
                                    continue
                                #プレイヤーの石と同色の石がある場合、石を置けるためのインデックスを保存
                                elif 4 <= x < 12 and 0 <= y < 8 and boards[y][x] == player:
                                    full_list.append((col,row))
                                    break
                                else:
                                    break
    return full_list
#石をひっくり返す
def full_pieces(col,row):
    for vx,vy in vec_table:
        flip_full_list = []
        x = vx + col
        y = vy + row
        while 4 <= x < 12 and 0 <= y < 8 and boards[y][x] == -player:
            flip_full_list.append((x,y))
            x += vx
            y += vy
            if 4 <= x < 12 and 0 <= y < 8 and boards[y][x] == player:
                for flip_x, flip_y in flip_full_list:
                    boards[flip_y][flip_x] = player
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
boards = [
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,1,-1,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,-1,1,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2],
    [2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2]]
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
            #フルスクリーン切り替え
            if starts.key == pygame.K_c:               
                full = pygame.display.toggle_fullscreen()
            #     pygame.display.set_mode((800, 800))
            # #フルスクリーン
            # if starts.key == pygame.K_f:
            #     pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)

                #フルスクリーン時の画面変更

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
            run = False
        if event.type == pygame.KEYDOWN:
            #ウインドウモード
            if event.key == pygame.K_c:
                pygame.display.set_mode((800, 800))
                fullscreen = False
            #フルスクリーン
            if event.key == pygame.K_f:
                full = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                fullscreen = True   
            if event.key == pygame.K_ESCAPE:
                run =False
                fullscreen = False
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
                    # if fullscreen:
                    #     x = mx // 100
                    #     y = my // 100
                    #     if board[y][x] == 0 and (x,y) in valid_position_list:
                    #         #石をひっくり返す
                    #         flip_pieces(x,y)
                    #         board[y][x] = player
                    #         player *= -1
                    #         pass_num = 0
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
    if fullscreen:
    #背景の塗りつぶし
    #full.fill(GREEN)
        #colが1だったら黒石を置いて-1だったら白石を置く設定
        for row_index,row in enumerate(boards):
            for col_index,col in enumerate(row):
                if col == 1:
                    pygame.draw.circle(full,BLACK,(col_index * square_size + 50, row_index * square_size + 100),45)
                elif col == -1:
                    pygame.draw.circle(full,WHITE,(col_index * square_size + 50, row_index * square_size + 100),45) 
        for i in range(square_num+1):
            for line in range(4):
                pygame.draw.line(full,GREEN,(0,line*square_size),(800,line*square_size),3)
                pygame.draw.line(full,GREEN,(line*square_size,0),(line*square_size,800),3)
            for line in range(4,9):
                pygame.draw.line(full,GREEN,(0,line*square_size),(800,line*square_size),3)
                pygame.draw.line(full,GREEN,(line*square_size,0),(line*square_size,50),3)
                pygame.draw.line(full,BLACK,(400,i*square_size+50),(1200,i*square_size+50),3)
                pygame.draw.line(full,BLACK,((i+4)*square_size,50),((i+4)*square_size,850),3)
        #石を置ける場所の取得
        full_list = full_potitions()
        #石を置ける場所を黄色の円で表示
        for x,y in full_list:
            pygame.draw.circle(full,YELLOW,(x * square_size + 50, y * square_size + 100),45,3)
        #イベントの取得     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                fullscreen = False
            #マウスクリック
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_over == False:
                    mx,my = pygame.mouse.get_pos()
                    x = mx // 100
                    y = my // 100
                    if boards[y][x] == 0 and (x,y) in full_list:
                        #石をひっくり返す
                        full_pieces(x,y)
                        boards[y][x] = player
                        player *= -1
                        pass_num = 0


                #横線 pygame.draw.line(screen,GREEN,(始点),(終点),3)   
    #更新
    pygame.display.update()
    clock.tick(FPS)
##################################################################################################

pygame.quit()