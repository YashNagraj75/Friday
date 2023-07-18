import voice,requests,bs4,webbrowser,speech 


class Search:
    def __init__(self) -> None:
        self.voice=voice.Voice()
        self.speech = speech.Synthesize()

    def automate_search(self,inp):
        """This model is used to automate the search process for the lazy developers like me."""

        # self.voice.speak('Googling it to get the best optimized results ....') # Giving it a niche touch !!!!!
        self.speech.The_Oracle('Googling it to get the best optimized results ....')
        results=100 # Minimum number of results to be displayed

        page=requests.get(f'https://www.google.com/search?q={inp}&num={results}')
        page.raise_for_status()
        soup=bs4.BeautifulSoup(page.text,'html.parser')
        links=soup.find_all('a') # Finding all the links on all the pages available.
        many=[]
        for link in links:
            href=link.get('href')
            if 'url?q=' in href and not 'webcache' in href:
                many.append(href.split('?q=')[1].split('&sa=U')[0])

        self.speech.The_Oracle(f'Found {len(many)} results, opening the top 5 results for you.')
        # no_of_results=int(input("Enter: "))
        webbrowser.open(f'https://www.google.com/search?q={inp}&num={results}')
        for i in range(5):
            webbrowser.open(many[i])

# search = Search()
# search.automate_search('pokemon')