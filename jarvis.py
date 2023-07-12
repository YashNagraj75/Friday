import openai,voice



class Friday:
    def __init__(self) -> None:
        self.key = openai.api_key = "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"
        self.model = "gpt-3.5-turbo"
        self.voice = voice.Voice()

    def LPU(self):
        while True:
            inp = input("Enter: ")
            completion  = openai.ChatCompletion.create(
                model = self.model,
                messages=[
                    {"role": "system", "content": inp},
                
                ]
            )
               
            
            print(completion.choices[0].message.content)



friday  = Friday()
friday.LPU()