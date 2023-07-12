import datetime,voice
import pywhatkit as kit

class Messanger:
    def __init__(self) -> None:
        self.voice=voice.Voice()
    
    def whatsapp(self,message,person):
        people={'papa': '+919686113665','mama': '+919110865120','sayli': '+919370933529'}
        hour=datetime.datetime.now().hour
        minute=datetime.datetime.now().minute
        
        if person in people.keys():
            self.voice.speak(f"Ok boss sending {person} a whatsapp message saying that {message}")
            kit.sendwhatmsg(people[person],message,hour,minute+1)
            
        else:
            self.voice.speak("Ok sir, will send the message but it seem's that the provided number is not on your contact list, should I still send the message Sir")
            input_to=input("Enter: ")
            if  input_to == 'yes':
                
                kit.sendwhatmsg(str(person),message,hour,minute+1)
    

# new = Messanger()
# new.whatsapp("Hello","papa")




