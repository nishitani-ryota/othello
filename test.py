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
        
pygame.init()

screen = pygame.display.set_mode((800,800))
screen.fill((0,100,0))
pygame.display.flip()
player =1
running = True



while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        draw = True        
        while draw:
            
            #最初のプレイヤーがクリックした箇所を白くする
            if player ==1:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x,y) = event.pos
                    (x,y) = makecircle(x,y)
                    player -= 1 
                    pygame.draw.circle(screen,(255,255,255),(x,y),50)
                    #pygame.display.flip()
                draw = False
                
            
            #次のプレイヤーがクリックした箇所を黒くする
            elif player == 0 :
                
                if event.type == pygame.MOUSEBUTTONDOWN:   
                    (x,y) = event.pos
                    (firstX,firstY) = (x,y) 
                    (x,y) = makecircle(x,y) 
                    player += 1
                    pygame.draw.circle(screen,(0,0,0),(x,y),50)
                    #pygame.display.flip()
                    #置いたマスの上下左右斜めをチェック
                    serch = [(x-100,y)]
                    list = []
                    change = True
                    (aa,bb) = (x-100,y)
                    
                    #一個左のマスと色が違って、そのマスのx座標が0以上であれば色を
                    for a in serch:
                        
                        #x=350のとき、250と色が違かったら、色を変えるためのリストに追加、その後250の左の駒も調べるため150にして調べるからserchの250の値を変える
                        if screen.get_at(a) != screen.get_at((x, y)) and x-100 > 0:
                            list.append(a)
                            (xx, yy) = (x-200,y)
                            updated_a =  (a[0] - 100, a[1])
                            #置いた左のマスが違う色の時、その左の駒が置いたマスと同じ色じゃないといけないので、xx<0かどうか調べる
                            if xx < 0 :
                                list = []
                                change = False
                            #上のif文でfalseにならなくて、下のif文で置いた石と２個左の駒が違う色ならupdated_aのx座標を-100して
                            while change:
                                if screen.get_at(updated_a) != screen.get_at((x, y)) and x-100 > 0:
                                    updated_a =  (updated_a[0] - 100, updated_a[1])
                                # print(updated_a)
                                elif screen.get_at(updated_a) == screen.get_at((x, y)) :
                                    change = False
                                elif updated_a[0] <= 0:
                                    list = []
                                    change = False
                            
                        if list:            
                            for b in list:
                                pygame.draw.circle(screen,(0,0,0),b,50)                                   
                    
                draw = False
        pygame.display.flip()

TODO:次はひっくり返すプログラムの作成


# 違う色のマスかどうか検索　
# 違う色だったら、それをリストに格納、それがあった方向＋１をしてまた検索　
# 違う色じゃなかったら検索終わり　
# そして、検索おわりまで出来たらリストの座標の駒の色を変換
    
    #pygame.time.Clock().tick(60)
#ゲーム終了
pygame.quit()
sys.exit()