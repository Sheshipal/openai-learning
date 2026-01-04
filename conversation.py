from openai import OpenAI

client = OpenAI()

# The Conversations API works with the Responses API to persist 
# conversation state as a long-running object with its own durable identifier. 
# After creating a conversation object, you can keep using it across sessions, devices, or jobs.
# Conversations store items, which can be messages, tool calls, tool outputs, and other data.

conversation_1 = client.conversations.create()
conversation_2 = client.conversations.create()

print(f"Conversation 1 - {conversation_1}")
print(f"Conversation 2 - {conversation_2}")

response_1 = client.responses.create(
    model="gpt-5-nano",
    input="What is the capital of India ?",
    conversation=conversation_1.id
)
print(f"Capital of India - {response_1.output_text}")

response_2 = client.responses.create(
    model="gpt-5-nano",
    input="What is the capital of Russia ?",
    conversation=conversation_2.id
)
print(f"Capital of Russia - {response_2.output_text}")

response_1 = client.responses.create(
    model="gpt-5-nano",
    input="What is the area of it ?",
    conversation=conversation_1.id
)
print(f"India capital area - {response_1.output_text}")

response_2 = client.responses.create(
    model="gpt-5-nano",
    input="What is the population of it ?",
    conversation=conversation_2.id
)
print(f"Russia capital population - {response_2.output_text}")