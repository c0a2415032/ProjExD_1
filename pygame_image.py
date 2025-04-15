import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.image.load("fig/pg_bg.jpg")#練習８
    kk_img = pg.image.load("fig/3.png")#練習２
    kk_rct = kk_img.get_rect()#レクトの取得　練習１０
    kk_rct.center = 300, 200#中心座標



    kk_img = pg.transform.flip(kk_img, True, False)
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習８

    tmr = 0
    x = tmr#練習６
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()#・キーの押下状態リストを取得
        

    
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])#練習６
        screen.blit(bg_img2, [-x+1600, 0])#練習７ 
        screen.blit(bg_img, [-x+3200, 0])#練習９
        screen.blit(kk_img, kk_rct)#練習４ １０


        pg.display.update()
        tmr += 1
      
        clock.tick(200)#練習５


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()