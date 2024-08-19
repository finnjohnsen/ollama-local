import json
import ollama
import asyncio
import psutil


def get_disk_used_percent() -> str:
  psutil.disk_usage('/').percent



async def run(model: str):
  client = ollama.AsyncClient()
  # Initialize conversation with a user query
  messages = [{'role': 'user', 'content': 'Hvilken flyplass er XFINX ?'}]

  # First API call: Send the query and function description to the model
  response = await client.chat(
    model=model,
    messages=messages,
    tools=tools,
  )

  # Add the model's response to the conversation history
  messages.append(response['message'])

  # Check if the model decided to use the provided function
  if not response['message'].get('tool_calls'):
    print("The model didn't use the function. Its response was:")
    print(response['message']['content'])
    return

  # Process function calls made by the model
  if response['message'].get('tool_calls'):
    available_functions = {
      'get_flight_times': get_flight_times,
      'get_airport_name_from_code': get_airport_name_from_code,
    }
    for tool in response['message']['tool_calls']:
      function_name = tool['function']['name']
      function_to_call = available_functions[function_name]
      print(f'Calling {function_name}' )
      if function_name == 'get_flight_times':
        function_response = function_to_call(tool['function']['arguments']['departure'], tool['function']['arguments']['arrival'])
      elif function_name == 'get_airport_name_from_code':
        print(f'Calling get_airport_name_from_code for {tool['function']['arguments']['airport_code']}')
        function_response = function_to_call(tool['function']['arguments']['airport_code'])
      else:
        function_response = None
      # Add function response to the conversation
      messages.append(
        {
          'role': 'tool',
          'content': function_response,
        }
      )

  # Second API call: Get final response from the model
  final_response = await client.chat(model=model, messages=messages)
  print(final_response['message']['content'])


# Run the async function
asyncio.run(run('llama3.1'))
