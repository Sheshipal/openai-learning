import os
import json
import requests
from openai import OpenAI

API_KEY = os.getenv("OWM_API_KEY")

def get_weather_info(place: str):
    geo_location_url = f"http://api.openweathermap.org/geo/1.0/direct?q={place}&appid={API_KEY}"
    
    response = requests.request("GET", geo_location_url)
    location_data = json.loads(response.text)
    lat = location_data[0]["lat"]
    lon = location_data[0]["lon"]

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

    response = requests.request("GET", weather_url)
    weather_data = json.loads(response.text)

    weather_short_desc = weather_data["weather"][0]["description"]
    weather_temp_kelvin = weather_data["main"]["temp"]
    weather_humidity = weather_data["main"]["humidity"]
    return (weather_short_desc, weather_temp_kelvin, weather_humidity)

def call_function(name, args):
    if name == "get_weather_info":
        return get_weather_info(**args)

tools = [
    {
        "type": "function",
        "name": "get_weather_info",
        "description": "Returns short description of weather, temparature in Kelvin and humidity of the given location.",
        "parameters":{
            "type": "object",
            "properties": {
                "place": {
                    "type": "string",
                    "description": "Place in - <location>,<state_code(optional)>,<country_code>. Ex - Kolkata,IN",
                },
            },
            "required": ["place"],
        }
    }
]

client = OpenAI()
conversation = client.conversations.create()
input_list = "I am in Hyderabad right now and travelling to Kolkata tonight, I would like to get the weather status for both the cities."

response = client.responses.create(
    model="gpt-5-nano",
    input=input_list,
    tools=tools,
    conversation=conversation.id,
)

input_list = []

for item in response.output:
    if item.type == "function_call":
         if item.name == "get_weather_info":
            weather_info = call_function(item.name, json.loads(item.arguments))
            
            # 4. Provide function call results to the model
            input_list.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": json.dumps({
                  "weather_info": weather_info
                })
            })

response = client.responses.create(
    model="gpt-5-nano",
    input=input_list,
    tools=tools,
    instructions="Consider the output from the tools while giving response",
    conversation=conversation.id,
)

print(response.output_text)