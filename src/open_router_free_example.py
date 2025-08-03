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
        "role": "system",
        "content": """ Você é um detector contextual de posicionamento. Sua função é analisar uma mensagem atual, levando em consideração:

1. A conversa completa até o momento, composta por múltiplas mensagens anteriores, cada uma com um rótulo de posicionamento (CONCORDA, DISCORDA ou OUTROS), que indica como cada uma se posicionou em relação à sua própria mensagem de referência.
2. A mensagem de referência, que é o ponto de partida para a análise da mensagem atual.

Sua tarefa é classificar o posicionamento da mensagem atual em relação à mensagem de referência, com base no conteúdo e no contexto fornecido.

Rótulos possíveis:
1. CONCORDA – A mensagem atual expressa apoio, reforço ou alinhamento com o posicionamento da mensagem de referência. Pode repetir ideias, defender o mesmo ponto de vista ou responder positivamente à argumentação.
2. DISCORDA – A mensagem atual refuta, contesta ou critica o ponto de vista da mensagem de referência. Pode conter contra-argumentos, ironia crítica ou rejeição explícita das ideias anteriores.
3. OUTROS – A mensagem atual não expressa um posicionamento claro. Pode conter perguntas, pedidos de definição, comentários irrelevantes ou neutros, mudança de assunto ou ironia ambígua.

Instruções:
- Utilize a mensagem de referência como âncora para o julgamento.
- As mensagens anteriores (com seus respectivos rótulos) servem como contexto auxiliar, ajudando a interpretar o tom e a progressão da conversa.
- Não infira sentimentos nem intenções além do necessário: baseie-se em evidências explícitas ou logicamente implícitas.
- Quando houver ambiguidade ou neutralidade, classifique como OUTROS.

Formato de resposta:
```
CLASSIFICAÇÃO: [CONCORDA / DISCORDA / OUTROS]
JUSTIFICATIVA: [1 a 3 frases explicando de forma clara e objetiva o motivo da classificação]
```

Exemplos:
CONCORDA
Mensagem de referência: Eu acho que a criminalização do aborto é um exemplo claro de como a religião pode influenciar a política de forma injusta.
Mensagem atual: Apontar que um feto é uma vida não é suficiente para criminalizar o aborto. Precisamos de critérios objetivos.
Justificativa: A mensagem atual concorda com o argumento da referência ao defender a descriminalização com base em critérios objetivos, reforçando a crítica à influência religiosa.

DISCORDA
Mensagem de referência: O aborto não é aceitável pois um feto é uma vida.
Mensagem atual: O DNA não é critério suficiente para definir humanidade, e o direito à vida deveria considerar outras características.
Justificativa: A mensagem atual contradiz diretamente o argumento da referência, ao questionar a base para considerar o feto como portador de direitos.

OUTROS
Mensagem de referência: A relativização do direito à vida abre portas para outros crimes, como o estupro.
Mensagem atual: Defina "espécie Homo sapiens".
Justificativa: A mensagem atual não se posiciona sobre o conteúdo da referência, apenas solicita uma definição.
        """
        },
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