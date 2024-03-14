import tkinter as tk
from ui import ui
from voice import Voice


def main():
    janela = tk.Tk()
    comando = Voice()
    ui(janela, comando)
    janela.mainloop()




if __name__ == "__main__":
    main()





   