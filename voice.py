import pyttsx3 ,datetime

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

    def greet(self):
        hour = datetime.datetime.now().hour
        if hour >= 0 and hour < 12:
            self.speak("Good Morning Sir")
        elif hour >= 12 and hour < 18:
            self.speak("Good Afternoon Sir")
        else:
            self.speak("Good Evening Sir")

# new = Voice()
# new.speak("Hello, I am Friday, your personal voice assistant. How may I help you today?")
