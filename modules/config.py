from openai import OpenAI
import os

# Ensure the API key is set
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai = OpenAI(
    api_key='Enter OpenAI API key here',
)

def get_gpt_response(user_input):
    message = {
        "role": "user",
        "content": user_input
    }

    response = openai.chat.completions.create(
        messages=[message],
        model="gpt-3.5-turbo-0125"
    )
    return response.choices[0].message.content
