import os
from openai import OpenAI

client = OpenAI(
    api_key = "e76c1633-14c0-4c05-ab0d-1f2a8312953c",
    base_url = "https://ark.cn-beijing.volces.com/api/v3",
)



def get_doubao(query):
    completion = client.chat.completions.create(
        model = "ep-20240731193438-fmfxd",  # your model endpoint ID
        messages = [
        {"role": "user", "content": query},
    ],
    )
    return completion.choices[0].message.content
    
if __name__ == "__main__":
    print(get_doubao("你好"))