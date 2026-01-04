from time import sleep
from openai import OpenAI
client = OpenAI()

# With background and stream set to true. We can stream the response.

stream = client.responses.create(
    model="gpt-5-nano",
    input="Write a 50 words essay on India in space.",
    background=True,
    stream=True
)

# Every event streamed has a predefined schema. Refer below links.
# https://platform.openai.com/docs/guides/streaming-responses
# https://platform.openai.com/docs/api-reference/responses-streaming
 
for event in stream:
    print(event)
