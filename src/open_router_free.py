from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

def chat_ai(prompt):
    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    )

    completion = client.chat.completions.create(
    model="google/gemma-3-27b-it:free",
    messages=[
        {
        "role": "user",
        "content": prompt
        }
    ]
    )

    print(completion.choices[0].message.content)

def main():
    while True:
        prompt = input("Prompt: ")
        chat_ai(prompt)

if __name__ == "__main__":
    main()