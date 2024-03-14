import speech_recognition as sr
import pyttsx3

class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.audio = pyttsx3.init()


    def ana (self):
        try:
            with sr.Microphone() as source:
                print("Ouvindo...")
                self.recognizer.adjust_for_ambient_noise(source) #Ajuste para ruido ambiete
                voz = self.recognizer.listen(source)
                print('executando...')


                comando = self.recognizer.recognize_google(voz, language="pt-BR")
                comando = comando.lower()
                print("comando reconnhecido", comando)


                if "ativar ana" in comando:
                    print('Asistente Ativa')
                    self.audio.say('Olá, tudo bem, eu sou a Ana')
                    self.audio.runAndWait()
                    return 'Assistente ativa com comando ' + comando
                else:
                    return "Comando reconhecido: + " + comando


        except sr.RequestError as e:
            print("Erro ao acessar serviço de reconhecimento de fala:", e)
            return "Erro de serviço"
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio")
            return "Áudio não entendido"
        
