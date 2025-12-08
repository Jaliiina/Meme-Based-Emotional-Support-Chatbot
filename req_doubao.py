import os
from openai import OpenAI

client = OpenAI(
    api_key = "",
    base_url = "",
)



def get_doubao(query):
    completion = client.chat.completions.create(
        model = "",  # your model endpoint ID
        messages = [
        {"role": "user", "content": query},
    ],
    )
    return completion.choices[0].message.content
    
if __name__ == "__main__":
    print(get_doubao("你好"))
