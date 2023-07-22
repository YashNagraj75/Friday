import Friday,voice,automate_search,phantom,backup,jokes,speech
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
        self.speech = speech.Synthesize()
        self.text = self.vox.hear()
        
    def reccognise_commmand(self):
        commands=[
            "Good bye friday",
            "Friday go to sleep",
        ]

    def incognito(self):
        while True:
            inp = input("Incognito mode: ")
            if(inp == "exit"):
                self.speech.The_Oracle("Exiting incognito mode")
                break      
            else:
                self.text = inp
                self.main()
                              
    def main(self ):
        """This is the main function which will be used to call all the other functions."""
        # self.speech.greet()
        # self.speech.The_Oracle("Initialising TTS engine.....")
        while True:
            text = self.text 
            # map = self.friday.LPU(f"Tell me if I want to see the map of a place or not answer in yes or no: {text} ")
            # info = self.friday.LPU(f"Can you tell me if I am trying to gather some information about someone or something, tell if yes or no only: {text} ")
            if "map" in text:
                place =self.friday.LPU(f"Give me only the name of the place in the given text: {text} ")
                self.phantom.map(place)

            elif "information" in text or "info" in text:
                search_element = self.friday.LPU(f"Give me the name of the search topic in the given text, give me only the topic name : {text} ")            
                self.speech.The_Oracle(f"Sure captain {self.friday.LPU(text)}")
                self.automate_search.automate_search(search_element)

            elif text.lower() == "friday sleep":
                self.speech.The_Oracle("Ok boss going to sleep have a good day ahead")
                break

            elif "joke" in text:
                joke = self.friday.LPU(f"Tell me if I want to hear a joke, if yes answer 'yes' else 'no'  : {text} ")
                if joke == "yes":
                    self.jokes.tell_jokes()

            elif text.lower() == "friday go incognito mode":
                self.speech.The_Oracle("Aye Captain going incognito")
                self.incognito()

            
            # else:
            #     self.speech.The_Oracle(self.friday.LPU(text))
            
                

        
    
main = Main()
main.main()





            
                

            

            
            
