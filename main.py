from urllib import response
import numpy as np
import speech_recognition as sr
from gtts import gTTS
import os
import datetime
import transformers



# Building the chatbot
class ChatBot():
    def __init__(self, name):
        print("--- Initializing", name, "---")
        self.name = name



    def speech_to_text(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration = 1)
            print("I am hearing......")
            audio = recognizer.listen(mic)

        try:
            self.text = recognizer.recognize_google(audio)
            print("User....", self.text)
        except:
            print("User.... Didnt Exactly get what you are saying!")

    @staticmethod
    def text_to_speech(text):
        print("Maneesha....", text)
        speaker = gTTS(text = text, lang = "en", slow = False)
        speaker.save("response.mp3")
        os.system("start res.mp3")
        os.remove("res.mp3")

    def wake_up(self, text):
        return True if self.name in text.lower() else False

    @staticmethod
    def action_time():
        return datetime.datetime.now().time().strftime('%H:%M')






# Initializing Maneesha
if __name__ == "__main__":
    ai = ChatBot(name="Maneesha")
    nlp = transformers.pipeline("conversational", model = "microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"

    while True:
        ai.speech_to_text()
        
        #Wake Up
        if ai.wake_up(ai.text) is True:
            response = "Hello this is Maneesha!!"
        
        elif "time" in ai.text:
            response = ai.action_time()

        elif any(i in ai.text for i in ["thank", "thanks"]):
            response = np.random.choice(["Anytime!","No Problem"])



        ai.text_to_speech(response)

