import speech_recognition as sr


class Voxtronix:
    def __init__(self) -> None:
        # Initialising  the recogniser
        self.recognise= sr.Recognizer()


    def hear(self):
        """This is the STT modle for Friday which will act as her ears and mouth"""        

        while(1):
            try:
                with sr.Microphone() as source2:
                    self.recognise.adjust_for_ambient_noise(source2,duration=0.1)

                    audio2=self.recognise.listen(source2)

                    Mytext= self.recognise.recognize_google(audio2)
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

# vox = Voxtronix()
# vox.hear() 