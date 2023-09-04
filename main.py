import pygame
import time
import random
from DeckOfCards import*

# display
pygame.init()
res = (1800, 1000)
WIN = pygame.display.set_mode(res)

pygame.display.set_caption("blecjec")

color = (0, 0, 244)
WIN.fill(color)

WIDTH = WIN.get_width()
HEIGHT = WIN.get_height()

pygame.display.flip()
clock = pygame.time.Clock()

bg = pygame.image.load(f'Poze Carti/BackGround/green-fabric-with-pattern-light-spots.jpg')
WIN.blit(bg, (0, 0))

t_font = pygame.font.SysFont('Arial', 30)
# card sizes
cH = 200
cL = 120

def isace(card):

        if card[1] =='4':
            return 1
        return 0

def drawOnScreen (player, size,x,y):
    i = 0

    while i < size:
        if player.isdealer and i == 1:
            card_image = pygame.image.load(f'Poze Carti/PNG/back.png')
            card_image = pygame.transform.scale(card_image, (cL, cH))
            WIN.blit(card_image, (x, y))
        else:
            WIN.blit(player.cardPhoto[i], (x, y))
        x += 180
        i += 1

def draw_text(text, font,text_col,x,y):
    txt = font.render(text, True, text_col)
    WIN.blit(txt, (x, y))

def draw_score(player, x, y):
    pygame.draw.rect(WIN,(255,255,255),pygame.Rect(x-75,y,200,50))
    if player.isdealer == False:
        draw_text(str(player.score), t_font, "black", x, y)
    else:
        draw_text(str(player.score - last_card_score(player)),t_font, "black", x, y)



def main():
    run = True

    pack = DeckOfCards()
    house = player()
    gambler = player()

    score_house_y = 360
    score_house_x = WIDTH/2-25
    score_gambler_y = HEIGHT/2 + 70
    score_gambler_x = WIDTH/2-25

    gamblerCardYstart = HEIGHT-350
    gamblerCardXstart = WIDTH/2-150
    houseCardYstart = 100
    houseCardXstart = WIDTH/2-150


    game_has_started = False
    game_has_ended = False
    while run == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if WIDTH / 2 - 75 <= mouse[0] <= WIDTH / 2 + 75 and HEIGHT / 2 - 30 <= mouse[1] <= HEIGHT / 2 + 30 and game_has_started == False and game_has_ended == False:
                    pack.make(pack.deck)
                    house.isdealer = True
                    WIN.blit(bg, (0, 0))
                    for i in range(4):
                        if i % 2 == 0:
                            gambler.score = pack.draw(pack.deck, gambler.hand, gambler.score)
                            if isace(gambler.hand[int(i/2)]):
                                gambler.nr_of_aces += 1

                        elif i % 2 == 1:
                            house.score = pack.draw(pack.deck, house.hand, house.score)
                            if isace(house.hand[int(i/2)]):
                                house.nr_of_aces += 1

                    if gambler.score == 22:
                        gambler.score = 12
                    if house.score == 22:
                        house.score = 12

                    # draw(gambler)
                    for i in range(2):
                        card_image = pygame.image.load(f'Poze Carti/PNG/{gambler.hand[i]}.png')
                        card_image = pygame.transform.scale(card_image, (cL, cH))
                        gambler.cardPhoto.append(card_image)

                    drawOnScreen(gambler, gambler.size, gamblerCardXstart, gamblerCardYstart)



                    # draw(house)
                    for i in range (2):
                        card_image = pygame.image.load(f'Poze Carti/PNG/{house.hand[i]}.png')
                        card_image = pygame.transform.scale(card_image, (cL, cH))
                        house.cardPhoto.append(card_image)

                    drawOnScreen(house, house.size, houseCardXstart, houseCardYstart)
                    game_has_started = True

                    draw_score(house, score_house_x, score_house_y)
                    draw_score(gambler, score_gambler_x, score_gambler_y)
                if game_has_started and WIDTH/2-165 < mouse[0] < WIDTH/2-15 and HEIGHT - 100 < mouse[1] < HEIGHT - 40:

                    WIN.blit(bg, (0, 0))
                    gamblerCardXstart -= 90

                    gambler.score = pack.draw(pack.deck, gambler.hand,gambler.score)
                    gambler.size += 1
                    if isace(gambler.hand[gambler.size-1]):
                        gambler.nr_of_aces += 1

                    if gambler.score > 21 and gambler.nr_of_aces > 0:
                        gambler.score -= 10
                        gambler.nr_of_aces -= 1

                    card_image = pygame.image.load(f'Poze Carti/PNG/{gambler.hand[gambler.size-1]}.png')
                    card_image = pygame.transform.scale(card_image, (cL, cH))
                    gambler.cardPhoto.append(card_image)

                    drawOnScreen(gambler, gambler.size, gamblerCardXstart, gamblerCardYstart)
                    drawOnScreen(house,house.size, houseCardXstart, houseCardYstart)
                    draw_score(house, score_house_x, score_house_y)
                    draw_score(gambler, score_gambler_x, score_gambler_y)

                    if(gambler.score>21):
                        lose_icon = pygame.image.load(f'Poze Carti/WinLose Models/lost.png')
                        WIN.blit(lose_icon, (WIDTH/2+300, HEIGHT/2-75))

                        another_game = pygame.image.load(f'Poze Carti/WinLose Models/newgame.png')
                        WIN.blit(another_game, (WIDTH/2-550, HEIGHT/2-75))

                        game_has_started = False

                        gambler = player()
                        house = player()

                        gamblerCardXstart = WIDTH / 2 - 150
                        game_has_ended = True

                if WIDTH / 2 - 550 < mouse[0] < WIDTH / 2 - 300 and HEIGHT / 2 - 75 < mouse[1] < HEIGHT / 2 + 75 and game_has_ended:
                    WIN.blit(bg, (0, 0))
                    game_has_ended = False

                if game_has_started and WIDTH/2+15 < mouse[0] < WIDTH/2+165 and HEIGHT - 100 < mouse[1] < HEIGHT - 40:
                    house.isdealer = False

                    WIN.blit(bg, (0, 0))

                    drawOnScreen(gambler, gambler.size, gamblerCardXstart, gamblerCardYstart)
                    drawOnScreen(house, house.size, houseCardXstart, houseCardYstart)
                    draw_score(house, score_house_x, score_house_y)
                    draw_score(gambler, score_gambler_x, score_gambler_y)



                    while(house.score<=16):

                        WIN.blit(bg, (0, 0))

                        houseCardXstart -= 90
                        house.score = pack.draw(pack.deck, house.hand, house.score)
                        house.size += 1

                        if isace(house.hand[house.size - 1]):
                            house.nr_of_aces += 1

                        if house.score > 21 and house.nr_of_aces > 0:
                            house.score -= 10
                            house.nr_of_aces -= 1


                        card_image = pygame.image.load(f'Poze Carti/PNG/{house.hand[house.size - 1]}.png')
                        card_image = pygame.transform.scale(card_image, (cL, cH))
                        house.cardPhoto.append(card_image)

                        drawOnScreen(gambler, gambler.size, gamblerCardXstart, gamblerCardYstart)
                        drawOnScreen(house, house.size, houseCardXstart, houseCardYstart)
                        draw_score(house, score_house_x, score_house_y)
                        draw_score(gambler, score_gambler_x, score_gambler_y)
                    if house.score>gambler.score and house.score<=21:
                        lose_icon = pygame.image.load(f'Poze Carti/WinLose Models/lost.png')
                        WIN.blit(lose_icon, (WIDTH / 2 + 300, HEIGHT / 2 - 75))

                        another_game = pygame.image.load(f'Poze Carti/WinLose Models/newgame.png')
                        WIN.blit(another_game, (WIDTH / 2 - 550, HEIGHT / 2 - 75))

                        game_has_started = False

                        gambler = player()
                        house = player()

                        houseCardXstart = WIDTH / 2 - 150
                        gamblerCardXstart=WIDTH/2 - 150


                        game_has_ended = True
                    elif house.score > 21:
                        win_icon = pygame.image.load(f'Poze Carti/WinLose Models/won.png')
                        WIN.blit(win_icon, (WIDTH / 2 + 300, HEIGHT / 2 - 75))

                        another_game = pygame.image.load(f'Poze Carti/WinLose Models/newgame.png')
                        WIN.blit(another_game, (WIDTH / 2 - 550, HEIGHT / 2 - 75))

                        game_has_started = False

                        gambler = player()
                        house = player()

                        houseCardXstart = WIDTH / 2 - 150
                        gamblerCardXstart = WIDTH / 2 - 150

                        game_has_ended = True
                    elif house.score < gambler.score:
                        win_icon = pygame.image.load(f'Poze Carti/WinLose Models/won.png')
                        WIN.blit(win_icon, (WIDTH / 2 + 300, HEIGHT / 2 - 75))

                        another_game = pygame.image.load(f'Poze Carti/WinLose Models/newgame.png')
                        WIN.blit(another_game, (WIDTH / 2 - 550, HEIGHT / 2 - 75))

                        game_has_started = False

                        gambler = player()
                        house = player()

                        houseCardXstart = WIDTH / 2 - 150
                        gamblerCardXstart = WIDTH / 2 - 150


                        game_has_ended = True
                    elif house.score == gambler.score:
                        win_icon = pygame.image.load(f'Poze Carti/WinLose Models/draw.png')
                        WIN.blit(win_icon, (WIDTH / 2 + 300, HEIGHT / 2 - 75))

                        another_game = pygame.image.load(f'Poze Carti/WinLose Models/newgame.png')
                        WIN.blit(another_game, (WIDTH / 2 - 550, HEIGHT / 2 - 75))

                        game_has_started = False
                        game_has_ended = True

                        gambler = player()
                        house = player()

                        houseCardXstart = WIDTH / 2 - 150
                        gamblerCardXstart = WIDTH / 2 - 150




        pygame.QUIT
        mouse = pygame.mouse.get_pos()


        startButton = pygame.image.load(f'Poze Carti/Buttons/StartButton.png')
        if game_has_started:
            standButton = pygame.image.load(f'Poze Carti/Buttons/StandButton.png')
            drawButton = pygame.image.load(f'Poze Carti/Buttons/DrawButton.png')
            WIN.blit(drawButton, (WIDTH / 2 - 165, HEIGHT - 100))
            WIN.blit(standButton, (WIDTH / 2 + 15, HEIGHT - 100))

        WIN.blit(startButton, (WIDTH/2-75, HEIGHT/2-30))
        pygame.display.update()

if __name__ == "__main__" :

    main()



