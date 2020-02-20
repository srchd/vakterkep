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

        self.win.blit(self.bg,(0,0))
        pygame.display.update()

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
        #print(self.var.get())
        if self.var.get() == 1:
            self.master.destroy()
            swiss = Countries(500, 324, "schweiz.jpg")
        elif self.var.get() == 2:
            self.master.destroy()
            austria = Countries(1152, 648, "oesterreich.png")
        elif self.var.get() == 3:
            self.master.destroy()
            germany = Countries(682, 862, "deutschland.png")

def main():
        root = Tk()
        mygui = WelcomeWindow(root)
        root.geometry("400x250+300+300")
        root.mainloop()

        run = True

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    main()
