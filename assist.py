import Friday,voice,automate_search,phantom,backup,jokes
import messanger as msg
import yagmail as email
import voxtronix as vox


class Main:
    def __init__(self):
        """This is the main class which will be used to call all the other classes."""
        self.friday = Friday.Friday()
        self.voice = voice.Voice()
        self.automate_search = automate_search.Search()
        self.phantom = phantom.Phantom()
        self.backup = backup.Backup()
        self.jokes = jokes.Chaplin()
        self.msg = msg.Messanger()
        self.vox = vox.Voxtronix()
        
    def reccognise_commmand(self):
        commands=[
            "Good bye friday",
            "Friday go to sleep",
        ]
    def main(self):
        """This is the main function which will be used to call all the other functions."""
        self.voice.greet()
        self.voice.speak("Initialising TTS engine.....")
        while True:
            text= self.vox.hear()
            map = self.friday.LPU(f"Tell me if I want to see the map of a place or not answer in yes or no: {text} ")
            if map.lower() =="yes":
                place =self.friday.LPU(f"Give me only the name of the place in the given text: {text} ")
                self.phantom.map(place)
            
            
                

        
    
main = Main()
main.main()





            
                

            

            
            
