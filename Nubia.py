# Importar as libs
import speech_recognition as sr

import pyttsx3

import os

from time import sleep

# Configurar a reprodução de voz e de reconhecimento

# Iniciar a lib
engine = pyttsx3.init()

# Definir a varíavel para escutar
microfone = sr.Recognizer()

# Iniciar loping while
while True:

    # Limpar códigos anteriores
    os.system("cls")

    # Definir Microphone em source
    with sr.Microphone() as source:

        # Ajustando microfone para tirar ruídos
        microfone.adjust_for_ambient_noise(source)
        
        # Pedir para falar algo
        print(".....")

        # Espaço
        print(" ")
        
        # Iniciar a escuta
        audio = microfone.listen(source)

        # Iniciar tentativas de reprodução de fala
        try:
            
            # Ajustar para escutar em portugês
            frase = microfone.recognize_google(audio, language = "pt-BR")

        # Exceção de erro
        except:
            
            # Definir o que irá ser dito
            engine.say("Não foi possível entender, tente novamente.")

            # Iniciar a fala
            engine.runAndWait()

            # Continuar
            continue
        
        # Caso tenha dado tudo certo
        else:
        
            # Mostrar o que foi dito
            print(": " + frase.lower())

            # Ínicio de comandos padrões

            # Se a frase for Nubia
            if frase.lower() == "núbia" or frase.lower() == "nubia":
                
                # Definir o que irá ser dito
                engine.say("Olá Deividi, como pósso ajudar?")

                # Iniciar a fala
                engine.runAndWait()

            # Se a frase for de encerrar    
            if frase.lower() == "sair" or frase.lower() == "encerrar" or frase.lower() == "fechar":

                # Definir o que irá ser dito
                engine.say("Entrando em modo de encerramento.")

                # Tempo para encerrar
                sleep(2)

                # Iniciar a fala
                engine.runAndWait()
 
                # Fechar o programa
                os.system("exit")

                # Parar o looping
                break

       
