import requests

API_KEY = "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"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
body = {
    "model": "text-davinci-003",
    "prompt": "Tell me some greate quote",
    "temperature": 0.8,
    "max_tokens": 100
}

quote = '\n\n"Life is not about waiting for the storm to pass, it\'s about learning to dance in the rain" - Vivian Greene'
def main():

    response = requests.post(
        url='https://api.openai.com/v1/completions',
        headers=headers,
        json=body
    )

    print(response.json()['choices'][0]['text'])


if __name__ == "__main__":
    main()
    # response = requests.get(url='https://api.openai.com/v1/models', headers=headers)
    # print(response.json())
