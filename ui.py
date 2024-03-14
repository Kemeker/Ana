import tkinter as tk


'''--------------------------------Interface da IA---------------------------------'''
def ui(janela, voice):
    janela.title("Ana Inteligencia Artificial")
    janela.geometry("500x600")
    janela.configure(background="#AFAFAF")

    start_button = tk.Button(janela, text='INICIAR', command=voice.ana)
    start_button.pack()

















