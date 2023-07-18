import voice,webbrowser,speech

class Phantom:
    def __init__(self) -> None:
        self.voice=voice.Voice()
        self.speech = speech.Synthesize()

    def map(self,place):
        """This model takes the place as input and opens the google maps in the browser"""
        # self.voice.speak(f"Okay boss, pulling up the map of {place}")
        self.speech.The_Oracle(f"Okay boss, pulling up the map of {place}")
        webbrowser.open(f'https:\\google.com\\maps\\place\\{place}')

    """ def track_loc(self,loc): 
    This is a work in progress model which will track my location  and look for any anaoamolies in the location and will send an SOS and many more features
    """




# phantom = Phantom()
# phantom.map('London')