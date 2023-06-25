import openai

class Jarvis:
    def __init__(self) -> None:
        self.key = "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"
        self.model = "gpt-3.5-turbo"

    def LPU(self,prompt):        
        openai.api_key = self.key

        response=openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "user","content": prompt}
            ],

            temperature=0.9,
        
            max_tokens=150
        )
        # print("hello")
        print(response.choices[0].message['content'])
        
       