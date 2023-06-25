import voice,requests,bs4,webbrowser


class Search:
    def __init__(self) -> None:
        self.voice=voice.Voice()

    def automate_search(self,inp):
        """This model is used to automate the search process for the lazy developers like me."""

        self.voice.speak('Googling it to get the best optimized results ....') # Giving it a niche touch !!!!!
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

        self.voice.speak(f'Found {len(many)} results how many do I display boss')
        no_of_results=int(input("Enter: "))
        for i in range(no_of_results):
            webbrowser.open(many[i])

# search = Search()
# search.automate_search('pokemon')