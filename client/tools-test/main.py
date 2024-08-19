import asyncio
import ollama

async def run(model: str):
    client = ollama.AsyncClient()
    print('Din ollama!')
    #while True:
    #    query = input("> ")
    #    print(f'Din query {query}')



#looper = asyncio.new_event_loop()
#looper.run_until_complete(run('llama3.1'))


#looper.stop()