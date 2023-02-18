import openai
import requests

import settings

# openai.api_key = settings.OPENAI_API_KEY


# def ask_chatgpt(question):
#     response = openai.Completion.create(
#         model="text-davinci-003",
#         prompt=question,
#         temperature=0.9,
#         max_tokens=1000,
#         top_p=1,
#         frequency_penalty=0.0,
#         presence_penalty=0.6,
#     )
#     return response['choices'][0]['text']


def ask_chatgpt(question):
    answer = ""

    headers = {
        "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "text-davinci-003",
        "prompt": question,
        "temperature": 0.9,
        "max_tokens": 1000,
        "top_p": 1,
        "frequency_penalty": 0.0,
        "presence_penalty": 0.6,
    }

    try:
        response = requests.post(
            url='https://api.openai.com/v1/completions',
            headers=headers,
            json=body
        )
        if response.status_code == 200:
            answer = response.json()['choices'][0]['text']
        else:
            answer = response.json()
    except Exception as e:
        print(e)
        answer = "Some error with OpenAI API: " + str(e)
    return answer



