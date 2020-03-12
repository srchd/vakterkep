import pygame
import os
from tkinter import *

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
    def correct(self, city, pos, cpos):
        if pos >= (45, 361) and pos <= (60, 376):
            pygame.draw.circle(self.win, (0,255,0), cpos, 5, 0)
        else:
            print("Nopie")

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
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # orszag vizsgalata utan szetszedni (au, sch, de)
                    #print(mygui.var.get())
                    #print(posx, posy)
                    pos = pygame.mouse.get_pos()
                    country.correct("Bregenz", pos, (54,371))
                    #pygame.draw.circle(country.win, RED, pos, 5, 0)

            if choice == 0:
                run = False
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    main()
