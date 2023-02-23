import openai
import os
import sys

##openai.api_key = YOUR_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_gpt(string):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=string,
            max_tokens=3000,
            temperature=0.6,
            frequency_penalty=1,
            presence_penalty=1
            )
    except openai.OpenAIError as error:
        raise print(f"Error: {str(e)}")

    try:
        answer = response["choices"][0]["text"]
    except(KeyError, IndexError) as error:
        pass
    print(answer)

chat_gpt(str(sys.argv[1:0]))
