import requests,bs4,random
urls=['https://www.funnyshortjokes.com/best-short-jokes','https://www.funnyshortjokes.com']
res=requests.get(random.choice(urls))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,'html.parser')
jokes=soup.find_all(class_='post-text')
many=[]
for joke in jokes:
    #print(joke.getText().strip())
    many.append(joke.getText().strip())

print(random.choice(many))