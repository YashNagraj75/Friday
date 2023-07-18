import os,zipfile,voice,datetime,send2trash,speech

class Backup:
    def __init__(self):
        self.voice = voice.Voice()
        self.speech = speech.Synthesize()
        
    def backup(self,folder):
        folder = os.path.abspath(folder) # Checking if it's an absolute path

        number = 1
        date = datetime.datetime.now()
        while True:
            zipFileName = os.path.basename(folder) + "_"+f"{date.day}_{date.month}_{date.year}"+".zip"
            if os.path.exists(zipFileName):
                
                break
            number +=1
            # self.voice.speak(f"Creating backup file of the folder {os.path.basename(folder)}")
            self.speech.The_Oracle(f"Creating backup file of the folder {os.path.basename(folder)}")
            backup = zipfile.ZipFile(zipFileName,'w') # Create the Zip file

            for folders,subfolders,filenames in os.walk(folder):
                print(f"Backing up {folders} ...")

                backup.write(folders)

                for file in filenames:
                    already= os.path.basename(folder) + "_"
                    if file.startswith(already) and file.endswith('.zip'):
                        continue
                    backup.write(os.path.join(folders,file))

            backup.close()






# back = Backup()
# back= back.backup('D:\\Python\\Friday')