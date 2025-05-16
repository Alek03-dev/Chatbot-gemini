!pip install google-genai

import os
from google.colab import userdata

os.environ['GOOGLE_API_KEY'] = userdata.get('GOOGLE_API_KEY')

from google import genai

client = genai.Client()

modelo = "gemini-2.0-flash"

resposta = client.models.generate_content(
    model=modelo,
    contents="Quem é a empresa por trás dos modelos Gemini"
)

resposta.text

chat = client.chats.create(model=modelo)

resposta = chat.send_message("Oi, tudo bem?")

resposta.text

resposta = chat.send_message("Você é um assistente pessoal e você sempre responde de forma sucinta. O que é inteligencia artificial?")

resposta.text

from google.genai import types

chat_config = types.GenerateContentConfig(
    system_instruction = "Você é um assistente pessoal e você sempre responde de forma sucinta.",
)

chat = client.chats.create(model=modelo, config=chat_config)

resposta = chat.send_message("O que é computação quantica?")

resposta.text

chat.get_history()

prompt = input("Esperando prompt: ")

while prompt != "fim":
  resposta = chat.send_message(prompt)
  __builtins__.print("Resposta: ", resposta.text) # Usando __builtins__.print
  __builtins__.print('\n')  # Usando __builtins__.print
  prompt = input("Esperando prompt: ")

  chat.get_history()

  chat_config_2 = types.GenerateContentConfig(
    system_instruction = "Você é um assistente pessoal que sempre responde de forma muito sarcastica",
)

chat_2 = client.chats.create(model=modelo, config=chat_config_2)