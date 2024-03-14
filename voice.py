import speech_recognition as sr
import pyttsx3

class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.audio = pyttsx3.init()
        self.text_updater = None

    def set_text_updater(self,updater):
        self.set_text_updater = updater        


    def ana (self):
        try:
            with sr.Microphone() as source:
                print("Ouvindo :) ")
                self.recognizer.adjust_for_ambient_noise(source) #Ajuste para ruido ambiete
                voz = self.recognizer.listen(source)
                self.update_text('Executando  :) ')


                comando = self.recognizer.recognize_google(voz, language="pt-BR").lower()
                
                if "ativar ana" in comando:
                    
                    resposta = 'Olá, tudo bem, eu sou a Ana'
                    self.update_text(resposta)
                    self.audio.say(resposta)
                    self.audio.runAndWait()
                    
                else:
                    resposta = 'Comando reconhecido ' + comando
                    self.update_text(resposta) #usando atualizador



        except sr.RequestError as e:
            mensagem_erro = "Erro ao acessar serviço de reconhecimento de fala: " + str(e)
            self.update_text(mensagem_erro)
        except sr.UnknownValueError:
            self.update_text("Não foi possível entender o áudio")
        

    def update_text(self, mensagem):
        if self.text_updater:
            self.text_updater(mensagem)