import pyttsx3,datetime



class Voice:
    def __init__(self) -> None:
        """Initializes the voice engine and sets the voice and rate to the desired values (0 is for male and 1 is for female prefer to have female voice as it sounds more natural)"""
        self.engine=pyttsx3.init()
        self.voice = self.engine.getProperty('voices')
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('voice',self.voice[1].id)
        self.engine.setProperty('rate',150)

    def speak(self,text):
        """This function takes the text as input and speaks it out"""
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()

    def greet(self):
        
        hour=datetime.datetime.now().hour
        if hour < 12:
            self.speak("Good morning Mr.Yash, I am Friday your personal voice assistant. How may I help you today")
        elif hour >=12 and hour<16:
            self.speak("Good afternoon Mr.Yash, I am Friday your personal voice assistant. How may I help you today")
        else:
            self.speak("Good evening Mr.Yash, I am Friday your personal voice assistant. How may I help you today")




# new = Voice()
# new.speak("Hello,Yash I am your assistant")

