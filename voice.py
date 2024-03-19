import speech_recognition as sr
import pyttsx3
from tempo import get_weather

class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.audio = pyttsx3.init()
        self.text_updater = None

    def set_text_updater(self,updater):
        self.text_updater = updater        


    def ana (self):
        try:
            with sr.Microphone() as source:
                print("Ouvindo...")
                self.recognizer.adjust_for_ambient_noise(source) #Ajuste para ruido ambiete
                voz = self.recognizer.listen(source)
                


                comando = self.recognizer.recognize_google(voz, language="pt-BR").lower()
                
                if "ativar ana" in comando:
                    
                    resposta = 'Olá, tudo bem, eu sou a Ana'
                    

                elif "temperatura" in comando:
                    city_name = "Chapecó"
                    api_key = 'cc97ce14bd7ad1f9faf2644f05a3b145'
                    temp_info = get_weather(api_key, city_name)

                    if 'erro' not in temp_info:
                        resposta = f"Em {temp_info['cidade']}, a temperatura é de {temp_info['temperatura']} graus Celsius, com {temp_info['descrição']}"        
                    
                    else:
                        resposta = 'Desculpe, nao conseguir obter a temperatura'
                else:
                    resposta = 'comando nao reconhecido'        

                self.update_text(resposta)
                self.audio.say(resposta)
                self.audio.runAndWait()    
                    





        except sr.RequestError as e:
            mensagem_erro = "Erro ao acessar serviço de reconhecimento de fala: " + str(e)
            self.update_text(mensagem_erro)
        except sr.UnknownValueError:
            self.update_text("Não foi possível entender o áudio")
        

    def update_text(self, mensagem):
        if self.text_updater:
            self.text_updater(mensagem)



           