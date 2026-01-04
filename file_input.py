# There are 3 ways to input pdf file data to model.
# 1. Using file URL
# 2. base64 encoded string
# 3. loading the file using client.files.create (Presented here)
# Refer - https://platform.openai.com/docs/guides/pdf-files

from openai import OpenAI
client = OpenAI()

file = client.files.create(
    file=open("Free_Test_Data_100KB_PDF.pdf", "rb"),
    purpose="user_data"
)

response = client.responses.create(
    model="gpt-5",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": file.id,
                },
                {
                    "type": "input_text",
                    "text": "Convert into English and summarise into 100 words?",
                },
            ]
        }
    ]
)

print(response.output_text)