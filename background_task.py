from time import sleep
from openai import OpenAI
client = OpenAI()

# With background set to true, request ID will be returned
# which can be used to retrive the status later point.
# Note: If we set background to true.
# 1. The response will be saved for ~10 mins.
# 2. There is no guarantee for ZDR(Zero Data Retention Policy).
response = client.responses.create(
    model="gpt-5-nano",
    input="Write a 50 words essay on India in space.",
    background=True
)

# This loop is for polling the response.
while response.status in ["queued", "in_progress"]:
    sleep(2)
    print("Waited for 2 seconds.")
    # Retrive the response after the wait period
    response = client.responses.retrieve(response.id)
print(response.output_text)


# # Cancelling a response which is in queue or in progress is possible.
# response = client.responses.cancel(response_id=response.id)
# print(response)