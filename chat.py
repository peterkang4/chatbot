from openai import OpenAI
import json


def load_api_key():
    print('loading api key...')
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        api_key = config['openai_api_key']
        print('api key is: ' + api_key)
        return api_key

client = OpenAI(api_key=load_api_key())

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
    {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
  ]
)

print(completion.choices[0].message)