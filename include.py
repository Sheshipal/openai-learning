from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-5-nano",
    input="Who is the current first citizen of India ?",
    include=["web_search_call.action.sources", "reasoning.encrypted_content"]
)

'''
Currently possible/supported values for include field:
web_search_call.action.sources: Includes the sources and URLs of a web search tool call in the response.
file_search_call.results: Includes the search results retrieved from your vector stores.
code_interpreter_call.outputs: Includes the outputs of Python code execution within the code interpreter tool call items.
reasoning.encrypted_content: Includes an encrypted version of the internal reasoning tokens, which can be useful for stateless multi-turn conversations.
message.output_text.logprobs: Includes log probabilities with assistant messages. 
'''

print(response.output_text)