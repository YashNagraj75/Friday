import os,zipfile,json,spotipy,base64,jarvis,voice,automate_search

import yagmail as email
import voxtronix as vox

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
    voice.speak(f"Creating backup file {zipFileName}")
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
    
    # creds= Credentials.from_authorized_user_file('credentials.json',['https://www.googleapis.com/auth/drive'])
    # # Create Drive API Client 
    # drive = build('drive','v3',credentials=creds)

    # """Now let's upload the backup to drive """
    # file_metadata={'name':zipFileName}
    # folder_id=None
    # if folder_id:
    #     file_metadata['parents']=[folder_id]
    # media=MediaFileUpload(os.path.abspath(zipFileName),resumable=True)
    # file=drive.files().create(body=file_metadata,media_body=media,feilds='id').execute()
    # print(f'File ID: {file.get("id")}')
    


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


        


def mail():
   
    login=email.SMTP('cleversquadtech@gmail.com','pwejkovsibyxaqfe')
    # login.send(to=reciever,subject=subject,contents=content)
    # login.close()
    # voice("Sending Email......")
    # voice("Email sent sucessfully")
        


        
    

def encode(file_name,output):
    base64.encode(file_name,output)



if __name__ =="__main__":    
    voice.greet()    
    while True:
        text=vox.Voxtronix.hear()
        print(text)
        if "map" in text:
            place=jarvis.Friday.LPU(f'Can you tell me only the place whose map I want to open in the this text:-{text}')
            map(str(place))
        if "Thank you Friday".lower() in text:
            voice("Your Welcome boss, hope you have a great day ahead")
            break
        if "search" in text or "look up" in text:
            search_element=LPU(f"Return only the search element in the text :- {text}")
            automate_search(search_element)

        if 'joke' in text:
           
            jokes()
           
        if "whatsapp" in text or 'message' in text:
            person=LPU(f'Tell me only the person I want to message in the text:- {text} ')
            message=LPU(f'Tell me only the message to be convayed in the text:- {text}')
            person=person.lower()
            print(person)
            whatsapp(message,person)

        elif 'email' in text or 'mail' in text:
            mail(text)
            
                

            

            
            
