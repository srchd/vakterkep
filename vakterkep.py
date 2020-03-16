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
        
        self.quit_button = Button(master, text="Quit", command=master.destroy)
        self.quit_button.pack()

        self.confirm_button = Button(master, text="Confirm", command=self.confirm)
        self.confirm_button.pack()

    def confirm(self):
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

#oe_cities = namedtuple("oe_cities", "city cpos minpos maxpos")
oe_cities = [
                [["Vorarlberg - Bregenz"], [(54, 371)], [(44,361)], [(64,381)]],
                [["Tirol – Innsbruck"], [(272,425)], [(262,415)], [(282,435)]]
            ]

def is_correct(pos, min_pos, max_pos):
    if pos >= min_pos and pos <= max_pos:
        return True
    else:
        return False

def main():
        root = Tk()
        mygui = WelcomeWindow(root)
        root.geometry("400x250+300+300")
        root.mainloop()

        run = True

        choice = mygui.var.get()
 
        if choice == 1:
            width = 1152
            height = 648

            country = Countries(width, height, "schweiz.jpg")
        elif choice == 2:
            width = 1152
            height = 648

            country = Countries(width, height, "oesterreich.png")

        elif choice == 3:
            width = 682
            height = 780

            country = Countries(width, height, "deutschland.png")

        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLACK = (0, 0, 0)
        r = random.SystemRandom()
        city = r.choice(range(2))
        font = pygame.font.Font(os.path.join("assets","LEMONMILK-Medium.otf"), 32)
        text = font.render(oe_cities[city][0][0], True, BLACK)
        textRect = text.get_rect()
        textRect.center = (country.width / 2, 20)
        while run:
            country.win.blit(text, textRect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    if is_correct(pos, oe_cities[city][2][0], oe_cities[city][3][0]):
                        pygame.draw.circle(country.win, GREEN, oe_cities[city][1][0], 5, 0)
                        city = r.choice(range(2))
                        text = font.render(oe_cities[city][0][0], True, BLACK)
                        textRect = text.get_rect()
                        textRect.center = (country.width / 2, 20)
                    else:
                        pygame.draw.circle(country.win, RED, oe_cities[city][1][0], 5, 0)
            if choice == 0:
                run = False
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    main()
