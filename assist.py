import os,zipfile,json,spotipy,webbrowser,base64,datetime,random,jarvis,voice
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload,MediaIoBaseUpload
import pywhatkit as kit
import yagmail as email
import speech_recognition as sr 

voice=voice.Voice()



        


def backupTo(folder):
    folder = os.path.abspath(folder) # ==> Checking if it's an absolute path 

    number = 1
    while True:
        zipFileName = os.path.basename(folder) + "_"+ str(number)+".zip"
        if not os.path.exists(zipFileName):
            break 
        number +=1

    # Create the Zip file 
    engine.say(f"Creating backup file {zipFileName}")
    backup = zipfile.ZipFile(zipFileName,'w')

    
        # Walk the folder tree and zip all the subfolders and files in the folder 
    for folder,subfolders,filenames in os.walk(folder):
        print(f"Backing up {folder} ...")

        backup.write(folder)

        for file in filenames:
            already= os.path.basename(folder) + "_"
            if file.startswith(already) and file.endswith('.zip'):
                continue
            backup.write(os.path.join(folder,file))

    backup.close()
    print(os.path.abspath(zipFileName))
    
    creds= Credentials.from_authorized_user_file('credentials.json',['https://www.googleapis.com/auth/drive'])
    # Create Drive API Client 
    drive = build('drive','v3',credentials=creds)

    """Now let's upload the backup to drive """
    file_metadata={'name':zipFileName}
    folder_id=None
    if folder_id:
        file_metadata['parents']=[folder_id]
    media=MediaFileUpload(os.path.abspath(zipFileName),resumable=True)
    file=drive.files().create(body=file_metadata,media_body=media,feilds='id').execute()
    print(f'File ID: {file.get("id")}')
    


def spotify():
    username = 'boodelyboo1234@gmail.com'
    clientID='eddb5451911e403f8f27d798368807f5' 
    clientsecret="24cd1cc3140e4b02a52d181ffbc9a6aa"
    redirect_uri='https://www.google.com/callback/'
    oauth_object=spotipy.SpotifyOAuth(clientID,clientsecret,redirect_uri)
    token_dict= oauth_object.get_access_token()
    token= token_dict['access_token']
    spoitfy=spotipy.Spotify(auth=token)
    user_name = spoitfy.current_user()

    print(json.dumps(user_name,sort_keys=True, indent=4)) # =>To read the response

    while True:
      print(f"Welcome to the project {user_name['display_name']}")
      u_input = int(input("Enter song"))
      if u_input == 1:
        song=input("Enter song")
        result = spoitfy.search(song,1,0,'track')
        songs_dict= result['tracks']
        song_items=songs_dict['items']
        song=song_items[0]['external_urls']['spotify']
        kit.search(song)
        print("Playing song")
      elif u_input == 0 :
        print("Exiting")

      else:
        print("Enter valid ")


def hear():
    r= sr.Recognizer()

    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2,duration=0.1)

                audio2=r.listen(source2)

                Mytext= r.recognize_google(audio2)
                Mytext=Mytext.lower()

                print(Mytext)
                #print(type(Mytext))
                return Mytext

        except sr.RequestError as e:
            print(f"Couldn't request because {e}")

        except sr.UnknownValueError :
            print("Unknown value error")
        
        except KeyboardInterrupt:
            break


def map(place):
    voice(f"Okay boss, pulling up the map of {place}")
    
    webbrowser.open(f'https:\\google.com\\maps\\place\\{place}')

def greet():
    hour=datetime.datetime.now().hour
    if hour < 12:
        voice("Good morning Mr.Yash, I am Friday your personal voice assistant. How may I help you today")
    elif hour >=12 and hour<16:
        voice("Good afternoon Mr.Yash, I am Friday your personal voice assistant. How may I help you today")
    else:
        voice("Good evening Mr.Yash, I am Friday your personal voice assistant. How may I help you today")

        
def whatsapp(message,person):
    people={'papa': '+919686113665','mama': '+919110865120','sayli': '+919370933529'}
    hour=datetime.datetime.now().hour
    minute=datetime.datetime.now().minute
   
    if person in people.keys():
        voice(f"Ok boss sending {person} a whatsapp message saying that {message}")
        
        
        kit.sendwhatmsg(people[person],message,hour,minute+1)
        
    else:
         voice("Ok sir, will send the message but it seem's that the provided number is not on your contact list, should I still send the message Sir")
         input_to=input("Enter: ")
         if  input_to == 'yes':
            
             kit.sendwhatmsg(str(person),message,hour,minute+1)


def mail():
   
    login=email.SMTP('cleversquadtech@gmail.com','pwejkovsibyxaqfe')
    # login.send(to=reciever,subject=subject,contents=content)
    # login.close()
    # voice("Sending Email......")
    # voice("Email sent sucessfully")
        

def jokes():
    
    urls=['https://www.funnyshortjokes.com/best-short-jokes','https://www.funnyshortjokes.com','https://www.funnyshortjokes.com/c/hilarious-jokes',"https://www.funnyshortjokes.com/c/racist-jokes","https://www.funnyshortjokes.com/c/dirty-jokes","https://www.funnyshortjokes.com/c/relationship-jokes","https://www.funnyshortjokes.com/c/yo-mama-jokes"]
    
    many=[]
    res=requests.get(random.choice(urls))
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    jokes=soup.find_all(class_='post-text')
    for joke in jokes:
        many.append(joke.getText().strip())
    voice(random.choice(many))
        
    

def encode(file_name,output):
    base64.encode(file_name,output)


# def image(prompt):
#     openai.api_key="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"

#     response=openai.Image.create(
#         prompt=prompt,
#         n=1,
#         size='512x512'
#     )

#     print(response['data'][0]['url'])
#     webbrowser.open(response['data'][0]['url'])
automate_search('Ronaldo')

# backupTo("C:\\Users\\ohm\\Desktop\\Learning\\Python")
# head = jarvis.Jarvis()
# head.LPU('hello')
#print(a.lower())
#potify()

# while True:
#      hear()

#greet()
#map('BDA Complex,Nagarbhavi,Banglore-560072')

#automate_search('')

#whatsapp('Hello papa sent this message using code','papa')
#mail()
#jokes('hilarious',0)

#encode(secret.txt,'secret.bin')
#image('Logo for a major tech company')

# if __name__ =="__main__":    
#     greet()    
#     while True:
#         text=hear()
#         print(text)
#         if "map" in text:
#             place=LPU(f'Can you tell me only the place whose map I want to open in the this text:-{text}')
#             map(str(place))
#         if "Thank you Friday".lower() in text:
#             voice("Your Welcome boss, hope you have a great day ahead")
#             break
#         if "search" in text or "look up" in text:
#             search_element=LPU(f"Return only the search element in the text :- {text}")
#             automate_search(search_element)

#         if 'joke' in text:
           
#             jokes()
           
#         if "whatsapp" in text or 'message' in text:
#             person=LPU(f'Tell me only the person I want to message in the text:- {text} ')
#             message=LPU(f'Tell me only the message to be convayed in the text:- {text}')
#             person=person.lower()
#             print(person)
#             whatsapp(message,person)

#         elif 'email' in text or 'mail' in text:
#             mail(text)
            
                

            

            
            
