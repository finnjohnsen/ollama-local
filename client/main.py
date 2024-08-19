from ollama import Client, AsyncClient
import asyncio

def syncChat():
    client = Client(host='http://localhost:11434')
    response = client.chat(model='llama3.1', messages=[
    {
        'role': 'user',
        'content': 'Why is the sky blue?',
    },
    ])
    print(response['message']['content'])


async def asyncChat():
    message = {'role': 'user', 'content': 'Why is the sky blue?'}
    async for part in await AsyncClient().chat(model='llama3.1', messages=[message], stream=True):
        print(part['message']['content'], end='', flush=True)
    print("\n")


#syncChat()
#asyncio.run(asyncChat())