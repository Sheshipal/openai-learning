from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini",
    input="tell me a joke",
)
print(response.output_text)

# Here we are passing the previous response id to the next request.
second_response = client.responses.create(
    model="gpt-4o-mini",
    previous_response_id=response.id,
    input="explain why this is funny.",
)
print(second_response.output_text)
