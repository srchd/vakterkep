import pygame
import os
from tkinter import *
from collections import namedtuple
import random

pygame.init()

class Countries:
    def __init__(self, width, height, img):
       # pygame.init()
        self.width = width
        self.height = height
        self.img = img
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load(os.path.join("assets",self.img))
        self.bg = pygame.transform.scale(self.bg,(self.width, self.height))

        self.win.blit(self.bg,(0,0))
        pygame.display.update()


    # majd tárolva így lesznek: város-cpos-minpos-maxpos

class WelcomeWindow:
    def __init__(self, master):
        self.started = False
        self.master = master
        master.title("Vaktérkép")

        self.label = Label(master, text="Vaktérképek: ")
        self.label.pack()

        #ez teszt

        self.var = IntVar()
        self.swiss = Radiobutton(master, text="Svájc", variable=self.var, value=1)
        self.swiss.pack(anchor=W)

        self.austr = Radiobutton(master, text="Ausztria", variable=self.var, value=2)
        self.austr.pack(anchor=W)

        self.germany = Radiobutton(master, text="Németország", variable=self.var, value=3)
        self.germany.pack(anchor=W)
        
        self.confirm_button = Button(master, text="Confirm", command=self.confirm)
        self.confirm_button.pack()

        self.quit_button = Button(master, text="Quit", command=master.destroy)
        self.quit_button.pack()

    def confirm(self):
        self.started = True
        self.width = 1152
        self.height = 648
        #choice = self.var.get()
        #print(self.var.get())
        if self.var.get() == 1:
            self.master.destroy()
            #500, 324
            #swiss = Countries(self.width,self.height , "schweiz.jpg")
        elif self.var.get() == 2:
            self.master.destroy()
            #1152, 648
            #austria = Countries(self.width, self.height, "oesterreich.png")
        elif self.var.get() == 3:
            self.master.destroy()
            #682, 862
            #germany = Countries(682, 780, "deutschland.png")
        else:
            print("Nem valasztottal orszagot!")

def is_correct(pos, min_pos, max_pos):
    if pos >= min_pos and pos <= max_pos:
        return True
    else:
        return False

def finished(succ):
    for x in succ:
        if x == 0:
            return False
    return True

def main():
        root = Tk()
        mygui = WelcomeWindow(root)
        root.geometry("400x250+300+300")
        root.mainloop()

        if not mygui.started:
            return

        run = True

        choice = mygui.var.get()
 
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLACK = (0, 0, 0)
        font = pygame.font.Font(os.path.join("assets","LEMONMILK-Medium.otf"), 32)

        if choice == 1:
            width = 1152
            height = 648
            c_range = 10
            cities = [
                [["Zürich - Zürich"], [(651, 140)], [(651 - c_range, 140 - c_range)], [(651 + c_range, 140 + c_range)]],
                [["Bern – Bern"], [(377, 272)], [(377 - c_range, 272 - c_range)], [(377 + c_range, 272 + c_range)]]
            ]
            in_range = len(cities)
            print("in_range:{}",in_range)
            succ = [0] * in_range

            country = Countries(width, height, "schweiz.jpg")

        elif choice == 2:
            width = 1152
            height = 648
            c_range = 10
            cities = [
                [["Vorarlberg - Bregenz"], [(54, 371)], [(54 - c_range, 371 - c_range)], [(54 + c_range, 371 + c_range)]],
                [["Tirol – Innsbruck"], [(272, 425)], [(272 - c_range, 425 - c_range)], [(272 + c_range, 425 + c_range)]]
            ]
            in_range = len(cities)
            print("in_range:{}",in_range)
            succ = [0] * in_range

            country = Countries(width, height, "oesterreich.png")

        elif choice == 3:
            width = 682
            height = 780
            c_range = 15
            cities = [
                [["Bayern – München"], [(426, 689)], [(426 - c_range, 689 - c_range)], [(426 + c_range, 689 + c_range)]],
                [["Baden-Württemberg"], [(249, 624)], [(249 - c_range, 624 - c_range)], [(249 + c_range, 624 + c_range)]]
            ]
            in_range = len(cities)
            print("in_range:{}",in_range)
            succ = [0] * in_range

            country = Countries(width, height, "deutschland.png")

        r = random.SystemRandom()
        city = r.choice(range(in_range))

        text = font.render(cities[city][0][0], True, BLACK)
        textRect = text.get_rect()
        if choice == 2:
            textRect.center = (int(country.width / 2), 20)
        else:
            textRect.topleft = (8, 8)

        snapshot = country.win.copy()

        score = 0

        while run:
            to_remove = country.win.blit(text, textRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if is_correct(pos, cities[city][2][0], cities[city][3][0]):
                        succ[city] = 1
                        country.win.blit(snapshot, to_remove, to_remove)
                        pygame.draw.circle(country.win, GREEN, cities[city][1][0], 5, 0)
                        score += 1
                        if not finished(succ):
                            temp_city = r.choice(range(in_range))
                            while temp_city == city:
                                temp_city = r.choice(range(in_range))
                            city = temp_city
                            text = font.render(cities[city][0][0], True, BLACK)
                            textRect = text.get_rect()
                            if choice == 2:
                                textRect.center = (int(country.width / 2), 20)
                            else:
                                textRect.topleft = (8, 8)
                        else:
                            run = False
                    else:
                        succ[city] = 1
                        country.win.blit(snapshot, to_remove, to_remove)
                        pygame.draw.circle(country.win, RED, cities[city][1][0], 5, 0)
                        if not finished(succ):
                            temp_city = r.choice(range(in_range))
                            while temp_city == city:
                                temp_city = r.choice(range(in_range))
                            city = temp_city
                            text = font.render(cities[city][0][0], True, BLACK)
                            textRect = text.get_rect()
                            if choice == 2:
                                textRect.center = (int(country.width / 2), 20)
                            else:
                                textRect.topleft = (8, 8)
                        else:
                            run = False
            if choice == 0:
                run = False
            pygame.display.update()
        pygame.quit()
        if finished(succ):
            print(score, "/", in_range) # majd tk_interbe írja ki, konzol nélküli program lesz

if __name__ == '__main__':
    main()
