import speech_recognition as sr
import pyttsx3
import pandas as pd
from tkinter import Canvas, PhotoImage, ttk
import tkinter as tk
import tkinter.ttk as ttk
import datetime as dt
import os
import tkinter.messagebox as msg
from PIL import ImageTk, Image



def ana ():
    '''Ana/IA'''

    audio = sr.Recognizer()
    ana = pyttsx3.init()

    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt_BR')
            comando = comando.lower()
            if 'ana' in comando:
                print(comando)
                ana.say('ola')
                ana.runAndWait()

    except:
        print('Microfone nao esta funcionando')   


'''-----------------------------Interface do programa----------------------------------------------------'''
aplication = tk.Tk()

aplication.title("Ana Inteligencia Artificial")
aplication.configure(background="#AFAFAF")
aplication.geometry("500x600")

botao = tk.Button(aplication, text='Chamar a Ana', command=ana)
botao.pack()

imagem = Image.open('image\\ia.jpg')  
photo = ImageTk.PhotoImage(imagem)

canvas1 = tk.Canvas(aplication, width=imagem.width, height=imagem.height)
canvas1.pack()


canvas1.create_image(0, 0, anchor=tk.NW, image=photo)



aplication.mainloop()



   