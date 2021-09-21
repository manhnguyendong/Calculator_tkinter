from tkinter import *
from tkinter.ttk import *
from view import View
from model import Model
class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()

    def display_btn(self):
        self.screen, self.button_frame = self.view.create_frame()
        self.view.create_button(self.button_frame)

    def config_command(self):
        length = len(self.view.list_button)
        self.view.list_button[length - 1]['command'] = self.view.root.quit
        self.view.list_button[0]['command'] = self.model.percentage
        self.view.list_button[1]['command'] = self.model.sqrt
        self.view.list_button[2]['command'] = self.model.square
        self.view.list_button[3]['command'] = self.model.invert
        self.view.list_button[4]['command'] = self.model.CE
        self.view.list_button[5]['command'] = self.model.C
def main():
    controller = Controller()
    controller.display_btn()
    controller.config_command()
    mainloop()

if __name__ == "__main__":
    main()