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
    '''Ana/IA'''

    audio = sr.Recognizer()
    ana = pyttsx3.init()

    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google_cloud(voz, language="pt_BR")
            comando = comando.lower()
            print("comando reconnhecido", comando)
            if "ativar ana" in comando:
                print('Assistete ativa')
                ana.say("Olá, tudo bem, eu sou a Ana")
                ana.runAndWait()
                comando = ' ' #reinnicia o comando apos a resposta da Ana

    except sr.RequestError as e:
        print("Erro ao acessar serviço de reconhecimento de fala:", e)
    except sr.UnknownValueError:
        print("Não foi possível entender o áudio")

    return comando   

ana()   

"""
def comando_voz_usuario():
    comando = ana()
    if "horas" in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        ana.say("Agora são" + hora)
        ana.runAndWait()



comando_voz_usuario()

"""



'''--------------------------------Interface da IA---------------------------------'''
'''
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


'''
   