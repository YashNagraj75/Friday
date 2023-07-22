import requests,bs4,random,voice,speech



class Chaplin:
    def __init__(self) -> None:
        self.urls =['https://www.funnyshortjokes.com/best-short-jokes','https://www.funnyshortjokes.com','https://www.funnyshortjokes.com/c/hilarious-jokes',"https://www.funnyshortjokes.com/c/racist-jokes","https://www.funnyshortjokes.com/c/dirty-jokes","https://www.funnyshortjokes.com/c/relationship-jokes","https://www.funnyshortjokes.com/c/yo-mama-jokes"]
        self.golden_times = []
        self.voice = voice.Voice()
        self.speech = speech.Synthesize()

    def tell_jokes(self):

        """
        A jokes model for the frustrating times and need some stress buster.
        The good old golden_times is back and will get updates very soon. 
        For the racist in you, we have a special section for you.
        """
        res=requests.get(self.urls[0])
        res.raise_for_status()
        # print(res)
        
        soup=bs4.BeautifulSoup(res.text,'html.parser')
        jokes=soup.find_all(class_='post-text')
        for joke in jokes:
            self.golden_times.append(joke.getText().strip())

        joke = random.choice(self.golden_times)
        # self.voice.speak(joke)
        self.speech.The_Oracle(joke)
        


# chap = Chaplin()
# chap.tell_jokes()







