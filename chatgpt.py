
from openai import OpenAI, AsyncOpenAI
import streamlit as st
import requests
import io

TOKEN = "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"

def read_key():
    try:
        f = open("key.txt","r")
    except:
        return False
    return f.readline()

class ChatBot:

    def __init__(self):
        api_key = read_key()
        self.client = OpenAI(api_key=api_key)


    

    def query(self,prompt):
   
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            
                {"role": "user", "content": prompt}
            ]
        )

        return completion.choices[0].message.content

    def create_image(self,prompt):
            
            API_URL = "https://api-inference.huggingface.co/models/prompthero/openjourney"
            headers = {"Authorization": f"Bearer {TOKEN}"}

            def query(payload):
                response = requests.post(API_URL, headers=headers, json=payload)
                return response.content
            image_bytes = query({
                "inputs": prompt,
            })
            return io.BytesIO(image_bytes)

    def create_prompt(self, selections):
        prompt = "Generate for me a short one-sentence prompt using simple words for AI to create a image having "
        for vn,en in selections.items():
            prompt += (en + ", ")
        prompt = prompt[:-2]
        prompt = self.query(prompt)
        #prompt += " in " + mode + " mode"
        return prompt
    


    def create_image_from_selections(self, selections):
        if(len(selections) == 0):
            return None
        prompt = self.create_prompt(selections)
        image = self.create_image(prompt)
        print(prompt)
        
        return image 

    def create_image_from_script(self, script):
        prompt = self.query(script)
        image = self.create_image(prompt)
        
        return image