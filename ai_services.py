import openai

import settings

openai.api_key = settings.OPENAI_API_KEY


def ask_chatgpt(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return response['choices'][0]['text']
