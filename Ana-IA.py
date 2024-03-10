import speech_recognition as sr
import pyttsx3
from turtle import bgcolor
from webbrowser import BackgroundBrowser
from numpy import imag
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
    ana = pyttsx3.init()

    '''-------- Dialogo da IA apos ser iniciada---------'''
    ana.say('Ola, eu sou a Ana, assistente virtual do Cristian')
    ana.say('Como posso te ajudar?')
    ana.say(' nao fala mais nada, já fiquei estressada')

    ana.runAndWait()


    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt_BR')
            comando = comando.lower()
            if 'ana' in comando:
                print(comando)

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



   