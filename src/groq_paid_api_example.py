import os
import dotenv
from groq import Groq

dotenv.load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)
def chat_ai(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
        temperature=1,
    )

    print(chat_completion.choices[0].message.content)

def main():
    while True:
        prompt = input("Prompt: ")
        chat_ai(prompt)

if __name__ == "__main__":
    main()

# é um serviço excelente, mas é pago a partir de um momento (não sei exatamente qual)
# vou montar o código pensando no open router, fazer testes com ele, e posteriormente posso alterar na hora de rodar tudo


# Acho que o modelo disponibilizado pela Groq não é dos melhores, eu quero utilizar um modelo do gemini
# Vou pesquisar se existe alguma outra maneira de usar os modelos gratuitos do google