import pygame
import os
from tkinter import *



class Swiss:
    def __init__(self):
        pygame.init()
        self.width = 500
        self.height = 324
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load(os.path.join("assets","schweiz.jpg"))

        self.win.blit(self.bg,(0,0))
        pygame.display.update()


class Germany:
    def __init__(self, win):
        self.win = win

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
            Swiss()

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
