import pyttsx3



class Voice:
    def __init__(self) -> None:
        self.engine=pyttsx3.init()
        self.voice = self.engine.getProperty('voices')
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('voice',self.voice[1].id)
        self.engine.setProperty('rate',175)

    def voice(self,text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()



