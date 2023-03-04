from decouple import config
import os
import openai
# ===================================================================================
openai.api_key = config("Key")
# ===================================================================================
def get_message(message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.8,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["stopfind"]
  )
  return(response['choices'][0]['text'])

def film_emogi(message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.8,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["stopfilm"]
  )
  return(response['choices'][0]['text'])


def horror_stories(message):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.8,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.5,
    presence_penalty=0.0
  )
  return(response['choices'][0]['text'])
# ===================================================================================
