import voice,requests,bs4,webbrowser


class Search:
    def __init__(self) -> None:
        self.voice=voice.Voice()

    def automate_search(self,inp):
        self.voice.speak('Googling it to get the best optimized results ....')
        results=100
        page=requests.get(f'https://www.google.com/search?q={inp}&num={results}')
        page.raise_for_status()
        soup=bs4.BeautifulSoup(page.text,'html.parser')
        links=soup.find_all('a')
        many=[]
        for link in links:
            href=link.get('href')
            if 'url?q=' in href and not 'webcache' in href:
                many.append(href.split('?q=')[1].split('&sa=U')[0])

        self.voice.speak(f'Found {len(many)} results how many do I display boss')
        no_of_results=int(input("Enter: "))
        for i in range(no_of_results):
            webbrowser.open(many[i])

