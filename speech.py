from elevenlabslib import *
import sounddevice,datetime
import random

class Synthesize:
  def __init__(self) -> None:
    self.api_key = "d6d686a2316036c8ac7f7f1fa1556458"
    self.user = ElevenLabsUser(self.api_key)
    self.voice = self.user.get_voices_by_name("Bella")[0]

  def select_output(self):
    outputDevices = [device for device in sounddevice.query_devices() if device["max_output_channels"] > 0]
    # for i in range(len(outputDevices)):
    #   print(outputDevices[i]['name'])  
    outputDevice = outputDevices[2]
    return outputDevice

  def The_Oracle(self,text):
    output = self.select_output()
    print(text)
    self.voice.generate_stream_audio_v2(text, PlaybackOptions(runInBackground=False, portaudioDeviceID=output['index']))
    
  
  def greet(self):
        hour = datetime.datetime.now().hour
        # self.The_Oracle("Hello, Master Yash I am Friday, your personal voice assistant. How may I help you today?")
        if hour >= 0 and hour < 12:
            self.The_Oracle("Good Morning Master Yash I am Friday, your personal voice assistant. How may I help you today?")
        elif hour >= 12 and hour < 18:
            self.The_Oracle("Good Afternoon Master Yash I am Friday, your personal voice assistant. How may I help you today?")
        else:
            self.The_Oracle("Good Evening Master Yash I am Friday, your personal voice assistant. How may I help you today?")

new = Synthesize()
new.select_output()