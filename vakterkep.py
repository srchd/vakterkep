import pygame
import os
from tkinter import *
from collections import namedtuple
import random

pygame.init()

class Countries:
    def __init__(self, width, height, img):
        self.width = width
        self.height = height
        self.img = img
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load(os.path.join("assets","bgs",self.img))
        self.bg = pygame.transform.scale(self.bg,(self.width, self.height))

        self.win.blit(self.bg,(0,0))
        pygame.display.update()

class FinishWindow:
    def __init__(self, master, out_str):
        master.title("Pontszám")

        self.label = Label(master, text=out_str)
        self.label.pack()

        self.quit_button = Button(master, text="Quit", command=master.destroy)
        self.quit_button.pack()

class WelcomeWindow:
    def __init__(self, master):
        self.started = False
        self.master = master
        master.title("Vaktérkép")

        self.label = Label(master, text="Vaktérképek: ")
        self.label.pack()

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

def is_correct(pos, min_pos, max_pos):
    if pos[0] >= min_pos[0] and pos[0] <= max_pos[0] and pos[1] >= min_pos[1] and pos[1] <= max_pos[1]:
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
        font = pygame.font.Font(os.path.join("assets","font","LEMONMILK-Medium.otf"), 20)

        if choice == 1:
            width = 1152
            height = 648
            c_range = 10
            cities = [
                [["Zürich - Zürich"], [(651, 140)], [(651 - c_range, 140 - c_range)], [(651 + c_range, 140 + c_range)]],
                [["Bern – Bern"], [(377, 272)], [(377 - c_range, 272 - c_range)], [(377 + c_range, 272 + c_range)]],
                [["Luzern – Lucerne"], [(593, 242)], [(593 - c_range, 242 - c_range)], [(593 + c_range, 242 + c_range)]],
                [["Altdorf – Uri"], [(682, 296)], [(682 - c_range, 296 - c_range)], [(682 + c_range, 296 + c_range)]],
                [["Schwyz – Schwyz"], [(674, 250)], [(674 - c_range, 250 - c_range)], [(674 + c_range, 250 + c_range)]],
                [["Obwalden – Sarnen"], [(582, 292)], [(582 - c_range, 292 - c_range)], [(582 + c_range, 292 + c_range)]],
                [["Nidwalden – Stans"], [(615, 271)], [(615 - c_range, 271 - c_range)], [(615 + c_range, 271 + c_range)]],
                [["Glarus – Glarus"], [(784, 250)], [(784 - c_range, 250 - c_range)], [(784 + c_range, 250 + c_range)]],
                [["Zug – Zug"], [(654, 204)], [(654 - c_range, 204 - c_range)], [(654 + c_range, 204 + c_range)]],
                [["Freiburg – Freiburg"], [(311, 324)], [(311 - c_range, 324 - c_range)], [(311 + c_range, 324 + c_range)]],
                [["Solothurn – Solothurn"], [(406, 188)], [(406 - c_range, 188 - c_range)], [(406 + c_range, 188 + c_range)]],
                [["Basel-Stadt – Basel"], [(426, 76)], [(426 - c_range, 76 - c_range)], [(426 + c_range, 76 + c_range)]],
                [["Basel-Landschaft – Liestal"], [(458, 111)], [(458 - c_range, 111 - c_range)], [(458 + c_range, 111 + c_range)]],
                [["Schaffhausen – Schaffhausen"], [(674, 35)], [(674 - c_range, 35 - c_range)], [(674 + c_range, 35 + c_range)]],
                [["Appenzell-Ausserrhoden – Herisau"], [(830, 136)], [(830 - c_range, 136 - c_range)], [(830 + c_range, 136 + c_range)]],
                [["Appenzell-Innerrhoden – Appenzell"], [(866, 149)], [(866 - c_range, 149 - c_range)], [(866 + c_range, 149 + c_range)]],
                [["St.Gallen – St.Gallen"], [(862, 120)], [(862 - c_range, 120 - c_range)], [(862 + c_range, 120 + c_range)]],
                [["Graubünden – Chur"], [(901, 302)], [(901 - c_range, 302 - c_range)], [(901 + c_range, 302 + c_range)]],
                [["Aargau – Aarau"], [(541, 132)], [(541 - c_range, 132 - c_range)], [(541 + c_range, 132 + c_range)]],
                [["Thurgau – Frauenfeld"], [(751, 77)], [(751 - c_range, 77 - c_range)], [(751 + c_range, 77 + c_range)]],
                [["Tessin – Bellinzona"], [(780 ,514)], [(780 - c_range ,514 - c_range)], [(780 + c_range ,514 + c_range)]],
                [["Waadt – Lausanne"], [(185, 410)], [(185 - c_range, 410 - c_range)], [(185 + c_range, 410 + c_range)]],
                [["Wallis – Sitten"], [(363, 500)], [(363 - c_range, 500 - c_range)], [(363 + c_range, 500 + c_range)]],
                [["Neuenburg- Neuenburg"], [(250, 257)], [(250 - c_range, 257 - c_range)], [(250 + c_range, 257 + c_range)]],
                [["Genf – Genf"], [(54, 508)], [(54 - c_range, 508 - c_range)], [(54 + c_range, 508 + c_range)]],
                [["Jura – Delsberg"], [(352, 148)], [(352 - c_range, 148 - c_range)], [(352 + c_range, 148 + c_range)]]
            ]
            in_range = len(cities)
            succ = [0] * in_range

            country = Countries(width, height, "schweiz.jpg")

        elif choice == 2:
            width = 1152
            height = 648
            c_range = 10
            cities = [
                [["Vorarlberg - Bregenz"], [(54, 371)], [(54 - c_range, 371 - c_range)], [(54 + c_range, 371 + c_range)]],
                [["Tirol – Innsbruck"], [(272, 425)], [(272 - c_range, 425 - c_range)], [(272 + c_range, 425 + c_range)]],
                [["Salzburg – Salzburg"], [(491, 322)], [(491 - c_range, 322 - c_range)], [(491 + c_range, 322 + c_range)]],
                [["Kärnten – Klagenfurt"], [(652, 221)], [(652 - c_range, 221 - c_range)], [(652 + c_range, 221 + c_range)]],
                [["Ober-Österreich – Linz"], [(657, 554)], [(657 - c_range, 554 - c_range)], [(657 + c_range, 554 + c_range)]],
                [["Steiermark – Graz"], [(804, 460)], [(804 - c_range, 460 - c_range)], [(804 + c_range, 460 + c_range)]],
                [["Nieder-Österreich – Sankt Pölten"], [(826, 239)], [(826 - c_range, 239 - c_range)], [(826 + c_range, 239 + c_range)]],
                [["Burgenland – Eisenstadt"], [(944, 302)], [(944 - c_range, 302 - c_range)], [(944 + c_range, 302 + c_range)]],
                [["Wien – Wien"], [(926, 232)], [(926 - c_range, 232 - c_range)], [(926 + c_range, 232 + c_range)]]
            ]
            in_range = len(cities)
            succ = [0] * in_range

            country = Countries(width, height, "oesterreich.png")

        elif choice == 3:
            width = 682
            height = 780
            c_range = 15
            cities = [
                [["Bayern – München"], [(426, 689)], [(426 - c_range, 689 - c_range)], [(426 + c_range, 689 + c_range)]],
                [["Baden-Württemberg"], [(249, 624)], [(249 - c_range, 624 - c_range)], [(249 + c_range, 624 + c_range)]],
                [["Saarland – Saarbrücken"], [(90, 579)], [(90 - c_range, 579 - c_range)], [(90 + c_range, 579 + c_range)]],
                [["Rheinland-Pfalz – Mainz"], [(184, 501)], [(184 - c_range, 501 - c_range)], [(184 + c_range, 501 + c_range)]],
                [["Hessen – Wiesbaden"], [(182, 492)], [(182 - c_range, 492 - c_range)], [(182 + c_range, 492 + c_range)]],
                [["Nordrhein-Westfalen – Düsseldorf"], [(74, 373)], [(74 - c_range, 373 - c_range)], [(74 + c_range, 373 + c_range)]],
                [["Thüringen – Erfurt"], [(386, 397)], [(386 - c_range, 397 - c_range)], [(386 + c_range, 397 + c_range)]],
                [["Sachsen – Dresden"], [(585, 392)], [(585 - c_range, 392 - c_range)], [(585 + c_range, 392 + c_range)]],
                [["Sachsen-Anhalt – Magdeburg"], [(431, 273)], [(431 - c_range, 273 - c_range)], [(431 + c_range, 273 + c_range)]],
                [["Brandenburg – Potsdam"], [(534, 247)], [(534 - c_range, 247 - c_range)], [(534 + c_range, 247 + c_range)]],
                [["Berlin – Berlin"], [(561, 233)], [(561 - c_range, 233 - c_range)], [(561 + c_range, 233 + c_range)]],
                [["Niedersachsen – Hannover"], [(291, 250)], [(291 - c_range, 250 - c_range)], [(291 + c_range, 250 + c_range)]],
                [["Bremen – Bremen"], [(222, 173)], [(222 - c_range, 173 - c_range)], [(222 + c_range, 173 + c_range)]],
                [["Hamburg – Hamburg"], [(310, 121)], [(310 - c_range, 121 - c_range)], [(310 + c_range, 121 + c_range)]],
                [["Mecklenburg-Vorpommern – Schwerin"], [(413, 113)], [(413 - c_range, 113 - c_range)], [(413 + c_range, 113 + c_range)]],
                [["Schleswig-Holstein – Kiel"], [(320, 32)], [(320 - c_range, 32 - c_range)], [(320 + c_range, 32 + c_range)]]
            ]
            in_range = len(cities)
            succ = [0] * in_range

            country = Countries(width, height, "deutschland.png")

        r = random.SystemRandom()
        city = r.choice(range(in_range))

        text = font.render(cities[city][0][0], True, BLACK)
        textRect = text.get_rect()
        if choice == 2:
            textRect.center = (int(country.width / 2), 20)
        elif choice == 3:
            textRect.topleft = (8, 60)
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
                    if is_correct(pos, cities[city][2][0], cities[city][3][0]):
                        succ[city] = 1
                        country.win.blit(snapshot, to_remove, to_remove)
                        pygame.draw.circle(country.win, GREEN, cities[city][1][0], 5, 0)
                        score += 1
                        if not finished(succ):
                            temp_city = r.choice(range(in_range))
                            while temp_city == city or succ[temp_city] == 1:
                                temp_city = r.choice(range(in_range))
                            city = temp_city
                            text = font.render(cities[city][0][0], True, BLACK)
                            textRect = text.get_rect()
                            if choice == 2:
                                textRect.center = (int(country.width / 2), 20)
                            elif choice == 3:
                                textRect.topleft = (8, 60)
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
                            while temp_city == city or succ[temp_city] == 1:
                                temp_city = r.choice(range(in_range))
                            city = temp_city
                            text = font.render(cities[city][0][0], True, BLACK)
                            textRect = text.get_rect()
                            if choice == 2:
                                textRect.center = (int(country.width / 2), 20)
                            elif choice == 3:
                                textRect.topleft = (8, 60)
                            else:
                                textRect.topleft = (8, 8)
                        else:
                            run = False
            if choice == 0:
                run = False
            pygame.display.update()
        pygame.quit()
        if finished(succ):
            out_str = 'Pontszámod: ' + str(score) + '/' + str(in_range)
            fin_root = Tk()
            fin_mygui = FinishWindow(fin_root, out_str)
            fin_root.geometry("400x250+300+300")
            fin_root.mainloop()


if __name__ == '__main__':
    main()
