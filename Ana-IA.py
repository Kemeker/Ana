import speech_recognition as sr
import pyttsx3
import pandas as pd
from tkinter import Canvas, PhotoImage, ttk
import tkinter as tk
import tkinter.ttk as ttk
import datetime 
import os
import tkinter.messagebox as msg
from PIL import ImageTk, Image


def ana ():
    

    audio = sr.Recognizer()
    ana = pyttsx3.init()

    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            audio.adjust_for_ambient_noise(source) #Ajuste para ruido ambiete
            voz = audio.listen(source)
            print('executando...')


            comando = audio.recognize_google(voz, language="pt-BR")
            comando = comando.lower()
            print("comando reconnhecido", comando)
            if "ativar ana" in comando:
                print('Asistente Ativa')
                ana.say('Olá, tudo bem, eu sou a Ana')
                ana.runAndWait()
                comando = ' ' #reinnicia o comando apos a resposta da Ana


    except sr.RequestError as e:
        print("Erro ao acessar serviço de reconhecimento de fala:", e)
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio")

    return comando   

'''--------------------------------Interface da IA---------------------------------'''

aplication = tk.Tk()

aplication.title("Ana Inteligencia Artificial")
aplication.configure(background="#AFAFAF")
aplication.geometry("500x600")

botao = tk.Button(aplication, text='INICIAR', command=ana)
botao.pack()

imagem = Image.open('image\\ia.jpg')  
photo = ImageTk.PhotoImage(imagem)

canvas1 = tk.Canvas(aplication, width=imagem.width, height=imagem.height)
canvas1.pack()


canvas1.create_image(0, 0, anchor=tk.NW, image=photo)



aplication.mainloop()




   