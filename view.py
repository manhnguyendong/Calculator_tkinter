from tkinter import *
from tkinter.ttk import *

class View:
    def __init__(self):
        self.root = Tk()
        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=4)
        self.root.geometry('400x400')
        self.root.title('Calculator')

    def create_frame(self):
        self.screen = Frame(self.root)
        self.screen.grid(column=0, row=0)
        self.keyboard = Frame(self.root)
        self.keyboard.grid(column=0, row=1)
        return self.screen, self.keyboard

    def create_button(self, frame_button):
        label = ['%', '√', 'x^2', '1/x', 'CE', 'C', 'Del', '/', '7', '8',
                 '9', 'x', '4', '5', '6', '-', '1', '2', '3', '+', '±',
                 '0', '.', '=', 'Quit']
        self.list_button = []
        rows = 5
        cols = 5
        cnt = 0
        for r in range(rows):
            for c in range(cols):
                self.button = Button(frame_button)
                self.button.grid(column=c, row=r, sticky=NSEW, padx=(5, 0), ipady=10)
                self.list_button.append(self.button)

        for (item, label_ele) in zip(self.list_button, label):
            item['text'] = label_ele

def main():
    # view = View()
    # screen, frame_button = view.create_frame()
    # view.create_button(frame_button)
    # mainloop()
    pass
if __name__ == "__main__":
    main()