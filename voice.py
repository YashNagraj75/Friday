import pyttsx3 

class Voice:
    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 190)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)


    def speak(self, text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()



new = Voice()
new.speak("Hello, I am Friday, your personal voice assistant. How may I help you today?")
