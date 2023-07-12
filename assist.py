import jarvis,voice,automate_search,phantom,backup,jokes
import messanger as msg
import yagmail as email
import voxtronix as vox

voice=voice.Voice()

def mail():
   
    login=email.SMTP('cleversquadtech@gmail.com','pwejkovsibyxaqfe')
    # login.send(to=reciever,subject=subject,contents=content)
    # login.close()
    # voice("Sending Email......")
    # voice("Email sent sucessfully")
        


        
    





if __name__ =="__main__":    
    voice.greet()    
    while True:
        text=vox.Voxtronix.hear()
        print(text)
        if "map" in text:
            place=jarvis.Friday.LPU(f'Can you tell me only the place whose map I want to open in the this text:-{text}')
            map(str(place))
        # if "Thank you Friday".lower() in text:
        #     voice("Your Welcome boss, hope you have a great day ahead")
        #     break
        # if "search" in text or "look up" in text:
        #     search_element=LPU(f"Return only the search element in the text :- {text}")
        #     automate_search(search_element)

        # if 'joke' in text:
           
        #     jokes()
           
        # if "whatsapp" in text or 'message' in text:
        #     person=LPU(f'Tell me only the person I want to message in the text:- {text} ')
        #     message=LPU(f'Tell me only the message to be convayed in the text:- {text}')
        #     person=person.lower()
        #     print(person)
        #     whatsapp(message,person)

        # elif 'email' in text or 'mail' in text:
        #     mail(text)
            
                

            

            
            
