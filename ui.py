import tkinter as tk
from tkinter import  scrolledtext
from voice import Voice


'''-------Area de texto----------------------------'''
def update_text_area(text_area, mensagem):
    text_area.configure(state='normal')
    text_area.insert(tk.END, mensagem + '\n')
    text_area.configure(state='disable')
    text_area.yview(tk.END)


'''--------Interface da IA------------------------'''
def ui(janela, voice):
    janela.title("Ana Inteligencia Artificial")
    janela.geometry("500x600")
    janela.configure(background="#AFAFAF")

    # Criando area de rolagem
    text_area = scrolledtext.ScrolledText(janela, state='disable', height=10)
    text_area.pack(pady=10)

    # Definindo o atualizador de texto
    def text_updater(mensagem):
        text_area.configure(state='normal')
        text_area.insert(tk.END, mensagem + "\n")
        text_area.configure(state='disable')
        text_area.yview(tk.END)

    voice.set_text_updater(lambda mensagem: update_text_area(text_area, mensagem))

    start_button = tk.Button(janela, text='INICIAR', command=voice.ana)
    start_button.pack()

    















