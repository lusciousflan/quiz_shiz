#coding:utf-8

import sys
import tkinter as tk

def sinx(screen, self):
    #global screen
    #global root
    print("Hello!")
    #screen = not screen
    if(screen == True):
        screen = False
    else:
        screen = True
    self.attributes('-fullscreen', screen)

def main():
    root = tk.Tk()

    root.title("test")

    root.geometry("400x300")
    
    root.attributes('-fullscreen', True)

    screen = True
    #button1 = tk.Button(root, command=sinx(screen, root), text="close")
    #button1.pack()
    
    root.bind('<Escape>', sinx(screen, root))
    
    root.mainloop()


if(__name__ == "__main__"):
    main()
