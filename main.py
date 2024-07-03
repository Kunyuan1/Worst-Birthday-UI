import pygame
import random
import time
import math
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]


def handtotal(lst):
    total = 0
    acecount = 0
    for x in range(len(lst)):
        if lst[x][0] == 11:
            total += 10
        elif lst[x][0] == 12:
            total += 10
        elif lst[x][0] == 13:
            total += 10
        elif lst[x][0] == 1:
            total += 1
            acecount += 1
        else:
            total += lst[x][0]
    for x in range(acecount):
        if total <= 11:
            total += 10
    return total

def isvalid(year, month, day):
    list1 = [1, 3, 5, 7, 8, 10, 12]
    if month == 0 or month > 12:
        return False
    if day > 31 or day == 0:
        return False
    if month not in list1 and day >= 31:
        return False
    elif month == 2 and day >= 30:
        return False
    elif month == 2 and day == 29:
        if year % 4 == 0:
            if year % 400 == 0:
                pass
            elif year % 100 == 0:
                return False
        else:
            return False
    return True
def deal():
    card = []
    card.append(numbers[random.randint(0, 12)])
    card.append(suits[random.randint(0, 3)])
    if card in dealt:
        return deal()
    else:
        dealt.append(card)
        return card


#Define the buttons
def create_button(text, x, y, width, height):
    return {'rect': pygame.Rect(x, y, width, height), 'text': text}

add_button = create_button("Add", 50, 150, 80, 40)
clear_button = create_button("Clear", 150, 150, 80, 40)
submit_button = create_button("Submit", 250, 150, 80, 40)

#Function to draw a button
def draw_button(button):
    pygame.draw.rect(scrn, GRAY, button['rect'])
    text_surf = BUTTON_FONT.render(button['text'], True, BLACK)
    text_rect = text_surf.get_rect(center=button['rect'].center)
    scrn.blit(text_surf, text_rect)

#Function to draw the current number
def draw_current_number(number):
    number_surf = FONT.render(str(number), True, BLACK)
    number_rect = number_surf.get_rect(center=(400 // 2, 50))
    scrn.blit(number_surf, number_rect)

#Function to draw the display box
def draw_display_box(display):
    display_str = ''.join(map(str, display))
    display_surf = FONT.render(display_str, True, BLACK)
    display_rect = display_surf.get_rect(center=(400 // 2, 250))
    scrn.blit(display_surf, display_rect)

#Function to handle button clicks
def handle_button_click(pos, display):
    if add_button['rect'].collidepoint(pos):
        return 'add'
    elif clear_button['rect'].collidepoint(pos):
        return 'clear'
    elif submit_button['rect'].collidepoint(pos):
        return 'submit'
    return None


pygame.init()
X = 700
Y = 400
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
green = (61, 145, 64)
status = True

scrn = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Birthdate Selection')
pygame.display.flip()

monthstart = False
daystart = False
yearstart = False

scrn.fill((255, 255, 255))
imp = pygame.image.load("Images/Board.jpg").convert()
monthtotal = 3
daytotal = 1
yeartotal = 2024
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
myFont = pygame.font.SysFont("Times New Roman", 18)
bigfont = pygame.font.SysFont("Times New Roman", 30)
verybigfont = pygame.font.SysFont("Times New Roman", 50)
NUMBER_FONT = pygame.font.Font(None, 60)
BUTTON_FONT = pygame.font.Font(None, 25)
FONT = pygame.font.Font(None, 50)
MESSAGE_FONT = pygame.font.Font(None, 40)
#initialization
betamount = ""
commence = False
collide = False
bet = False
cycle = False
start = False
player = []
dealt = []
dealer = []
stand = False
bust = False
gameend = False
win = False
submitted = False
display = []
submit_message = ""
number = random.randint(1, 10000000)

#Button class
class Button:
    def __init__(self, text, x, y, width, height, action):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.action = action

    def draw(self, scrn):
        pygame.draw.rect(scrn, GRAY, self.rect)
        text_surf = BUTTON_FONT.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        scrn.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

#Button actions
def multiply_by_3(n):
    return n * 3

def add_7(n):
    return n + 7

def divide_by_5(n):
    return n / 5

def subtract_2(n):
    return n - 2

def floor_number(n):
    return math.floor(n)

def square_root(n):
    return math.sqrt(n)

def square(n):
    return n ** 2

def log_number(n):
    return math.log(n)

def cube_root(n):
    return n ** (1/3)

def submit_number(n):
    return n, True

#Create buttons
buttons = [
    Button("Multiply by 3", 100, 200, 120, 40, multiply_by_3),
    Button("Add 7", 240, 200, 120, 40, add_7),
    Button("Divide by 5", 380, 200, 120, 40, divide_by_5),
    Button("Subtract 2", 100, 260, 120, 40, subtract_2),
    Button("Floor", 240, 260, 120, 40, floor_number),
    Button("Square Root", 380, 260, 120, 40, square_root),
    Button("Square", 100, 320, 120, 40, square),
    Button("Log", 240, 320, 120, 40, log_number),
    Button("Cube Root", 380, 320, 120, 40, cube_root),
    Button("Submit", 240, 400, 120, 40, submit_number),
]



while (status):
    for i in pygame.event.get():
        if monthstart == True:
            start = True
            if cycle == False:
                scrn.fill(white)
            
            date = myFont.render(f"Current Month Selected: {months[monthtotal-1]}", 1, red)
            info = myFont.render(f'Win Rounds to Advance in Months', 1, red)
            cont = myFont.render("Press Anywhere to Continue", 3, red)
            if bet == False:
                if monthtotal <= 0:
                    monthtotal = 1
                if monthtotal >= 13:
                    monthtotal = 12
                scrn.fill((green))
                scrn.blit(info, (175, 10))
                scrn.blit(date, (175, 50))
                scrn.blit(cont, (175, 150))
                mouse = pygame.mouse.get_pos()
                pygame.draw.rect(scrn, red, [50, 50, 75, 50], 2)
                home = myFont.render("Home", 1, red)
                scrn.blit(home, (55, 62))
                pygame.display.flip()
                if i.type == pygame.MOUSEBUTTONDOWN:
                    if 50 < mouse[0] < 100 and 50 < mouse[1] < 100:
                        start = False
                        monthstart = False
                        cycle = False
                        continue
                    else:
                        bet = True
            if bet == True:
                if cycle == False:
                    scrn.fill(white)
                    imp = pygame.image.load("Images/Board.jpg").convert()
                    scrn.blit(imp, (0, 0))
                    money = myFont.render(f"Your month: {months[monthtotal-1]}", 1, red)
                    scrn.blit(money, (450, 0))

                    if commence == False:
                        if i.type == pygame.MOUSEBUTTONDOWN:
                            commence = True
                    else:
                        end = True
                        win = False
                        if not player:
                            player.append(deal())
                            player.append(deal())
                        if not dealer:
                            dealer.append(deal())
                            dealer.append(deal())
                        for x in range(len(player)):
                            playercard = pygame.image.load('Images/' + player[x][1] + '-' + str(player[x][0]) + '.svg')
                            playercard = pygame.transform.scale(playercard, (75, 110))
                            scrn.blit(playercard, (300 + x * 25, 250))
                            pygame.display.flip()
                            time.sleep(0.5)
                        dealercard = pygame.image.load("Images/CardBack.png")
                        dealercard = pygame.transform.scale(dealercard, (75,110))
                        scrn.blit(dealercard, (225, 20))
                        pygame.display.flip()
                        time.sleep(0.5)
                        for x in range(1, len(dealer)):
                            dealercard = pygame.image.load("Images/" + dealer[x][1] + "-" + str(dealer[x][0]) + ".svg")
                            dealercard = pygame.transform.scale(dealercard, (75,110))
                            scrn.blit(dealercard, (300 + x * 25, 20))
                            pygame.display.flip()
                        scrn.blit(myFont.render("HIT", 1, red), (150, 300))
                        scrn.blit(myFont.render("STAND", 1, red), (530, 300))
                        hit_box = pygame.Rect(100, 300, 140, 32)
                        stand_box = pygame.Rect(500, 300, 140, 32)
                        pygame.draw.rect(scrn, red, hit_box, 2)
                        pygame.draw.rect(scrn, red, stand_box, 2)
                        pygame.display.flip()
                        cycle = True
                else:
                    if i.type == pygame.MOUSEBUTTONDOWN:
                        print("MOUSEDOWN")
                        if hit_box.collidepoint(i.pos):
                            hit = True
                            player.append(deal())
                            playercard = pygame.image.load('Images/' + player[-1][1] + '-' + str(player[-1][0]) + '.svg')
                            playercard = pygame.transform.scale(playercard, (75, 110))
                            scrn.blit(playercard, (300 + len(player) * 25, 250))
                            pygame.display.flip()
                            if handtotal(player) > 21:
                                scrn.blit(verybigfont.render("You busted!", 1, red), (200, 150))
                                pygame.display.flip()
                                time.sleep(1)
                                win = False
                                gameend = True
                                
                        elif stand_box.collidepoint(i.pos):
                            while handtotal(dealer) < 17:
                                dealer.append(deal())
                                dealercard = pygame.image.load('Images/' + dealer[-1][1] + '-' + str(dealer[-1][0]) + '.svg')
                                dealercard = pygame.transform.scale(dealercard, (75, 110))
                                scrn.blit(dealercard, (300 + len(dealer) * 25, 20))
                                pygame.display.flip()
                                time.sleep(0.5)
                            if handtotal(dealer) > 21:
                                dealercard = pygame.image.load('Images/' + dealer[0][1] + '-' + str(dealer[0][0]) + '.svg')
                                dealercard = pygame.transform.scale(dealercard, (75, 110))
                                scrn.blit(dealercard, (225, 20))
                                scrn.blit(verybigfont.render("Dealer Busted!", 1, red), (150, 150))
                                win = True
                                gameend = True
                            if gameend == False:
                                if handtotal(dealer) > handtotal(player):
                                    dealercard = pygame.image.load('Images/' + dealer[0][1] + '-' + str(dealer[0][0]) + '.svg')
                                    dealercard = pygame.transform.scale(dealercard, (75, 110))
                                    scrn.blit(dealercard, (225, 20))
                                    scrn.blit(verybigfont.render("Dealer Wins!", 1, red), (200, 150))
                                    gameend = True
                                    win = False
                                else:
                                    dealercard = pygame.image.load('Images/' + dealer[0][1] + '-' + str(dealer[0][0]) + '.svg')
                                    dealercard = pygame.transform.scale(dealercard, (75, 110))
                                    scrn.blit(dealercard, (225, 20))
                                    scrn.blit(verybigfont.render("You Win!", 1, red), (225, 150))
                                    gameend = True
                                    win = True
                            pygame.display.flip()
                            time.sleep(1)
                    if gameend == True:
                        if win == True:
                            monthtotal += 1
                        else:
                            monthtotal -= 1
                        #reset
                        commence = False
                        collide = False
                        bet = False
                        betamount = ""
                        player = []
                        dealt = []
                        dealer = []
                        cycle = False
                        stand = False
                        gameend = False
                        continue
                        pygame.display.flip()
            pygame.display.flip()
            if i.type == pygame.QUIT:
                status = False

        
        elif daystart == True:
            if i.type == pygame.MOUSEBUTTONDOWN:
                for button in buttons:
                    if button.is_clicked(i.pos):
                        if button.text == "Submit":
                            daytotal, submitted = button.action(current_number)
                        else:
                            daytotal = button.action(daytotal)
            scrn.fill(white)

            #Render the number
            number_surf = myFont.render(f"{daytotal:.5f}", True, black)
            number_rect = number_surf.get_rect(center=(700/2, 400/6))
            scrn.blit(number_surf, number_rect)

            #Draw the buttons
            for button in buttons:
                button.draw(scrn)

            #Display the submission message if the number has been submitted
            if submitted:
                submission_surf = myFont.render(f"Your date is: {current_number:.5f}", True, black)
                submission_rect = submission_surf.get_rect(center=(700/2, 5 * 400/6))
                scrn.blit(submission_surf, submission_rect)
            pygame.draw.rect(scrn, red, [50, 50, 75, 50], 2)
            home = myFont.render("Home", 1, red)
            scrn.blit(home, (55, 62))
            pygame.display.flip()
            if i.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                print(mouse)
                if 50 < mouse[0] < 125 and 50 < mouse[1] < 100:
                    start = False
                    daystart = False
                    cycle = False
                    continue
            # Update the display
            pygame.display.flip()

        elif yearstart == True:
            scrn.fill(WHITE)
            current_number = random.randint(0, 9)

            #current number
            draw_current_number(current_number)

            #buttons
            draw_button(add_button)
            draw_button(clear_button)
            draw_button(submit_button)

            #display box
            draw_display_box(display)
            
            #submit message if present
            if submit_message:
                submit_surf = MESSAGE_FONT.render(submit_message, True, BLACK)
                submit_rect = submit_surf.get_rect(center=(400 // 2, 700 - 30))
                scrn.blit(submit_surf, submit_rect)

            pygame.display.flip()
            if i.type == pygame.MOUSEBUTTONDOWN:
                action = handle_button_click(i.pos, display)
                if action == 'add' and len(display) < 4:
                    display.append(current_number)
                elif action == 'clear':
                    display = []
                    submit_message = ""
                elif action == 'submit' and len(display) == 4:
                    yeartotal = int(f'{display[0]}{display[1]}{display[2]}{display[3]}')
                    yearstart = False
                    start = False
                    cycle = False
                    continue
        
        else:
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(scrn, red, [50, 50, 75, 50], 2)
            home = myFont.render("Home", 1, red)
            scrn.blit(home, (55, 62))
            pygame.display.flip()
            if i.type == pygame.MOUSEBUTTONDOWN:
                if 50 < mouse[0] < 100 and 50 < mouse[1] < 100:
                    start = False
                    monthstart = False
                    cycle = False
                    continue
            if start == False:
                if cycle == False:
                    welcome = myFont.render("ENTER BIRTHDATE HERE!", 1, black)
                    scrn.fill(white)
                    scrn.blit(welcome, (200, 50))
                    pygame.draw.rect(scrn, black, [130, 150, 150, 50], 2)
                    month = myFont.render(f'{months[monthtotal-1]}', 1, black)
                    scrn.blit(month, (140, 160))
                    pygame.draw.rect(scrn, black, [305, 150, 70, 50], 2)
                    day = myFont.render(f'{daytotal}', 1, black)
                    scrn.blit(day, (315, 160))
                    pygame.draw.rect(scrn, black, [400, 150, 100, 50], 2)
                    year = myFont.render(f'{yeartotal}', 1, black)
                    scrn.blit(year, (410, 160))
                    if i.type == pygame.MOUSEBUTTONDOWN:
                        if 130 < mouse[0] < 280 and 150 < mouse[1] < 200:
                            monthstart = True
                        elif 305 < mouse[0] < 375 and 150 < mouse[1] < 200:
                            daystart = True
                        elif 400 < mouse[0] < 500 and 150 < mouse[1] < 200:
                            yearstart = True
            
    pygame.display.flip()

pygame.quit()