from openai import OpenAI
import os
import dotenv

dotenv.load_dotenv()

# def chat_ai(prompt):
#     client = OpenAI(
#     base_url="https://openrouter.ai/api/v1",
#     api_key=os.getenv("OPENROUTER_API_KEY"),
#     )

#     completion = client.chat.completions.create(
#     model="google/gemma-3-27b-it:free",
#     temperature=0.0,
#     top_p=1.0,
#     messages=[
#         {
#         "role": "system",
#         "content": """ Você é um detector contextual de posicionamento. Sua função é analisar uma mensagem atual, levando em consideração:

# 1. A conversa completa até o momento, composta por múltiplas mensagens anteriores, cada uma com um rótulo de posicionamento (CONCORDA, DISCORDA ou OUTROS), que indica como cada uma se posicionou em relação à sua própria mensagem de referência.
# 2. A mensagem de referência, que é o ponto de partida para a análise da mensagem atual.

# Sua tarefa é classificar o posicionamento da mensagem atual em relação à mensagem de referência, com base no conteúdo e no contexto fornecido.

# Rótulos possíveis:
# 1. CONCORDA – A mensagem atual expressa apoio, reforço ou alinhamento com o posicionamento da mensagem de referência. Pode repetir ideias, defender o mesmo ponto de vista ou responder positivamente à argumentação.
# 2. DISCORDA – A mensagem atual refuta, contesta ou critica o ponto de vista da mensagem de referência. Pode conter contra-argumentos, ironia crítica ou rejeição explícita das ideias anteriores.
# 3. OUTROS – A mensagem atual não expressa um posicionamento claro. Pode conter perguntas, pedidos de definição, comentários irrelevantes ou neutros, mudança de assunto ou ironia ambígua.

# Instruções:
# - Utilize a mensagem de referência como âncora para o julgamento.
# - As mensagens anteriores (com seus respectivos rótulos) servem como contexto auxiliar, ajudando a interpretar o tom e a progressão da conversa.
# - Não infira sentimentos nem intenções além do necessário: baseie-se em evidências explícitas ou logicamente implícitas.
# - Quando houver ambiguidade ou neutralidade, classifique como OUTROS.

# Formato de resposta:
# ```
# CLASSIFICAÇÃO: [CONCORDA / DISCORDA / OUTROS]
# JUSTIFICATIVA: [1 a 3 frases explicando de forma clara e objetiva o motivo da classificação]
# ```

# Exemplos:
# CONCORDA
# Mensagem de referência: Eu acho que a criminalização do aborto é um exemplo claro de como a religião pode influenciar a política de forma injusta.
# Mensagem atual: Apontar que um feto é uma vida não é suficiente para criminalizar o aborto. Precisamos de critérios objetivos.
# Justificativa: A mensagem atual concorda com o argumento da referência ao defender a descriminalização com base em critérios objetivos, reforçando a crítica à influência religiosa.

# DISCORDA
# Mensagem de referência: O aborto não é aceitável pois um feto é uma vida.
# Mensagem atual: O DNA não é critério suficiente para definir humanidade, e o direito à vida deveria considerar outras características.
# Justificativa: A mensagem atual contradiz diretamente o argumento da referência, ao questionar a base para considerar o feto como portador de direitos.

# OUTROS
# Mensagem de referência: A relativização do direito à vida abre portas para outros crimes, como o estupro.
# Mensagem atual: Defina "espécie Homo sapiens".
# Justificativa: A mensagem atual não se posiciona sobre o conteúdo da referência, apenas solicita uma definição.
#         """
#         },
#         {
#         "role": "user",
#         "content": prompt
#         }
#     ]
#     )

#     print(completion.choices[0].message.content)

# def main():
#     while True:
#         prompt = input("Prompt: ")
#         chat_ai(prompt)

# if __name__ == "__main__":
#     main()

# quando inserido no terminal, o prompt user não pode ter enter, uma vez que o enter é entendido como um sinal de envio de mensagem
# quando inserido via código, o prompt user pode utilizar o enter, uma vez que ainda é a mesma string

########################################################################## exemplo de inserção via código ##########################################################################

# client = OpenAI(
# base_url="https://openrouter.ai/api/v1",
# api_key=os.getenv("OPENROUTER_API_KEY"),
# )

# completion = client.chat.completions.create(
# model="google/gemma-3-27b-it:free",
# temperature=0.0,
# top_p=1.0,  
# messages=[
#     {
#     "role": "system",
#     "content": """ Você é um detector contextual de posicionamento. Sua função é analisar uma mensagem atual, levando em consideração:

# 1. A conversa completa até o momento, composta por múltiplas mensagens anteriores, cada uma com um rótulo de posicionamento (CONCORDA, DISCORDA ou OUTROS), que indica como cada uma se posicionou em relação à sua própria mensagem de referência.
# 2. A mensagem de referência, que é o ponto de partida para a análise da mensagem atual.

# Sua tarefa é classificar o posicionamento da mensagem atual em relação à mensagem de referência, com base no conteúdo e no contexto fornecido.

# Rótulos possíveis:
# 1. CONCORDA – A mensagem atual expressa apoio, reforço ou alinhamento com o posicionamento da mensagem de referência. Pode repetir ideias, defender o mesmo ponto de vista ou responder positivamente à argumentação.
# 2. DISCORDA – A mensagem atual refuta, contesta ou critica o ponto de vista da mensagem de referência. Pode conter contra-argumentos, ironia crítica ou rejeição explícita das ideias anteriores.
# 3. OUTROS – A mensagem atual não expressa um posicionamento claro. Pode conter perguntas, pedidos de definição, comentários irrelevantes ou neutros, mudança de assunto ou ironia ambígua.

# Instruções:
# - Utilize a mensagem de referência como âncora para o julgamento.
# - As mensagens anteriores (com seus respectivos rótulos) servem como contexto auxiliar, ajudando a interpretar o tom e a progressão da conversa.
# - Não infira sentimentos nem intenções além do necessário: baseie-se em evidências explícitas ou logicamente implícitas.
# - Quando houver ambiguidade ou neutralidade, classifique como OUTROS.

# Formato de resposta:
# ```
# CLASSIFICAÇÃO: [CONCORDA / DISCORDA / OUTROS]
# JUSTIFICATIVA: [1 a 3 frases explicando de forma clara e objetiva o motivo da classificação]
# ```

# Exemplos:
# CONCORDA
# Mensagem de referência: Eu acho que a criminalização do aborto é um exemplo claro de como a religião pode influenciar a política de forma injusta.
# Mensagem atual: Apontar que um feto é uma vida não é suficiente para criminalizar o aborto. Precisamos de critérios objetivos.
# Justificativa: A mensagem atual concorda com o argumento da referência ao defender a descriminalização com base em critérios objetivos, reforçando a crítica à influência religiosa.

# DISCORDA
# Mensagem de referência: O aborto não é aceitável pois um feto é uma vida.
# Mensagem atual: O DNA não é critério suficiente para definir humanidade, e o direito à vida deveria considerar outras características.
# Justificativa: A mensagem atual contradiz diretamente o argumento da referência, ao questionar a base para considerar o feto como portador de direitos.

# OUTROS
# Mensagem de referência: A relativização do direito à vida abre portas para outros crimes, como o estupro.
# Mensagem atual: Defina "espécie Homo sapiens".
# Justificativa: A mensagem atual não se posiciona sobre o conteúdo da referência, apenas solicita uma definição.
#     """
#     },
#     {
#     "role": "user",
#     "content": """
# ### CONVERSA (com rótulos anteriores):\n\
# [1] Pessoa A - RAIZ: Eu acho que a descriminalização do aborto é uma questão de saúde pública.\n\
# [2] Pessoa B - RESPONDE A [1]: Mas isso ignora o direito do feto à vida. [DISCORDA]\n\
# [3] Pessoa C - RESPONDE A [2]: Nem todo feto é viável; devemos considerar o caso da mãe. [CONCORDA]\n\
# [4] Pessoa D - RESPONDE A [3]: Você poderia explicar o que você quer dizer com 'viável'? [OUTROS]\n\
# \n\
# ### MENSAGEM ATUAL:\n\
# Pessoa E - RESPONDE A [2]: Direito à vida de quem exatamente? Porque quando a mãe morre por um aborto clandestino, ninguém parece se importar.\n\
# \n\
# ### MENSAGEM DE REFERÊNCIA:\n\
# [1] Pessoa A - RAIZ: Eu acho que a descriminalização do aborto é uma questão de saúde pública.\n\
# \n\
# Classifique o posicionamento da **mensagem atual** com relação à **mensagem de referência**. Leve em consideração todo o contexto.
# """
#     }
# ]
# )

# print(completion.choices[0].message.content)
                                                                          
####################################################################################################################################################################################

# teste de um prompt gerado pelo conjunto de dados
# foi utilizada a maior conversa, e mesmo assim não estourou a janela de contexto do modelo

client = OpenAI(
base_url="https://openrouter.ai/api/v1",
api_key=os.getenv("OPENROUTER_API_KEY"),
)

completion = client.chat.completions.create(
model="google/gemma-3-27b-it:free",
temperature=0.0,
top_p=1.0,  
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
    "content": """
### CONVERSA (com rótulos anteriores):
[1] MENSAGEM RAIZ: Eu acho que a pessoa que é contra o aborto está usando uma lógica moralista e religiosa para justificar sua posição, mas isso não é uma razão objetiva para negar o direito das mulheres de tomar decisões sobre seu próprio corpo. Além disso, se considerarmos o feto como vida, então teríamos que aplicar a mesma lógica para outras questões, como a masturbação, que poderia ser considerada um genocídio se considerarmos a vida do feto como uma vida humana. Isso mostra que a lógica usada para justificar a proibição do aborto é inconsistente e não pode ser aplicada de forma justa e igualitária
[2] Danielle_Cannon - RESPONDE A [1]: De fato, mas acredito que fetos são vivos, o que não implica que devem ter o direito de continuar nesse estado. Aliás, não apenas o ato de ejacular seria um genocídio, mas simplesmente limpar o chão também seria, se todas as formas de vida tivessem o mesmo peso nas nossas concepções. [CONCORDA]
[3] David_Fuller - RESPONDE A [2]: Ser um ser vivo é completamente irrelevante. Um macaco é um ser vivo e nem por isso ele deve deter qualquer um dos direitos que qualquer ser humano detêm. O que vale é se é um ser humano [DISCORDA]
[4] Roy_Ross - RESPONDE A [2]: Um embrião não é um feto. [DISCORDA]
[5] Beverly_Black - RESPONDE A [1]: [deleted] [DISCORDA]
[6] Shawn_Bell - RESPONDE A [5]: é um tubo pequeninho na vdd [OUTROS]
[7] Matthew_Davenport - RESPONDE A [1]: Quando o espermatozoide encontra o óvulo, ali nasce uma vida, ali ela começa a ser gerada e vai se desenvolvendo estágiopor estágio. O esperma sozinho é so uma semente, que se nao entrar na terra nunca brotará para virar uma árvore. Um broto debaixo da terra nao é uma arvore ainda mas ja esta no processo. ( tirá-lo da terra alegando que ele nao é uma planta ainda é ironia pq ele ja é mas só esta começando) . Uma semente no lixo ou uma terra sem semente não são o começo de uma planta, somente é quando se juntam os dois. O mesmo é espermatozoide e ovulo.  Sua mae precisava ser religosa pra saber que mesmo que ela nao quisesse te ter ela poderia te parir no minimo? pq a vontade dela nao está acima da sua vida! A pessoa que esta ainda em formação precisa ter a chance de viver a vida dela também mesmo que nao seja na casa e sob a proteção e educação de quem a gerou. [DISCORDA]
[8] Kayla_Robinson - RESPONDE A [7]: Cara, você tem que separar sua opinião e visão do que é biologicamente fato e também o que é filosoficamente a vida, o que é vida, biologicamente um feto de algumas semanas não é vida, ele não tem todos os meios fisiológicos para estar vivo sozinho (oq muitas vezes caracteriza vida), filosoficamente o feto, não tem consciência de estar vivo, portanto também não dá pra considerar vivo, sem contar algumas vertentes que tb levam em consideração que o feto deve ser considerado vivo apartir do momento que sente dor(que tem receptores nervosos) que é a muitas semanas dentro da gestação. Outro ponto é, se você não pode intervir numa outra vida, pois a sua vontade não está a cima da outra, põe que você mata animais para consumo, ou ainda, por que come plantas, plantas são vivas, animais são vivos, esse conceito é mais complexo do que o "vida é isso é não pode mexer", como exemplifiquei, vida varia de ponto científico, filosofico, não há consenso, por isso quando o aborto é falado, o principal a considerar é, a pessoa que quer abortar. [CONCORDA]
[9] Jamie_Hayes - RESPONDE A [8]: >Outro ponto é, se você não pode intervir numa outra vida, pois a sua vontade não está a cima da outra, põe que você mata animais para consumo  Errado, para sociedade a vida de um ser humano não tem o mesmo valor que a vida de animais, plantas, etc. Não faz nem sentido comparar uma coisa com a outra. [DISCORDA]
[10] Haley_Nguyen - RESPONDE A [9]: Mas aí você parte do pressuposto que o feto que vale por um ser humano [OUTROS]
[11] Christopher_George - RESPONDE A [9]: Então por que um **feto** teria o mesmo valor de uma **vida** **humana**? Só porque tem "potencial" para ser uma vida humana? Porque o cérebro de um feto só **começa** a se desenvolver a partir da 6ª semana e só desenvolve partes mais importantes até a 12ª semana e ainda tem partes que vão continuar se desenvolvendo, isso sem contar que o bebê só seria capaz de possivelmente sobreviver fora do útero só a partir da 24ª semana. [CONCORDA]
[12] Jamie_Hayes - RESPONDE A [11]: Então, tudo se resume ao que você considera como vida humana. O dilema em torno do feto e sua potencialidade é comparável ao desafio de delimitar a fronteira entre a física quântica e a física clássica - é uma área confusa. Vamos pensar em termos de probabilidade. Se você observar uma pedra por 10 anos, qual é a chance de ela se transformar em um ser humano? Provavelmente próxima de zero. E se observar um feto de um cachorro pelo mesmo período? Igualmente improvável. Mas, e se observar um feto humano durante esses 10 anos? As chances de vê-lo crescer e se tornar uma criança são maiores que 95%.  Isso nos leva a perguntar: nossa humanidade não é definida pela totalidade desse processo de desenvolvimento, em vez de apenas um ponto específico onde tudo começa? [DISCORDA]
[13] Christopher_George - RESPONDE A [12]: Mas o feto humano **depende** de um humano para tornar-se humano. Eu tô falando de consciência humana que é resultante de um cérebro humano, resultando assim em um humano, um feto não **é** humano porque **ser** é diferente de **poder ser**. [CONCORDA]
[14] Jamie_Hayes - RESPONDE A [13]: >Mas o feto humano **depende** de um humano para tornar-se humano  Não entendi qual é seu ponto com essa frase.  >Eu tô falando de consciência humana que é resultante de um cérebro humano, resultando assim em um humano, um feto não **é** humano porque **ser** é diferente de **poder ser**.  Então pra você em que ponto se tornamos humanos? ser humano é imutável? A partir do momento que X coisa acontece você é um ser humano e isso não pode ser mudado, talvez apenas com a morte. O que é isso para você?  Um bebê que nasce com algum tipo de deficiência que impede ele de ter conciência, mas mesmo assim cresce e se desenvolve, ele é um ser humano ou não?  >um feto não **é** humano porque **ser** é diferente de **poder ser**.  Então, o ponto é justamente que você e nem ninguém consegue dizer em qual momento a vida começa, em exatamente o que **pode ser** começa a **ser,** isso em um sentido filosófico e ético, porque segundo a biologia a vida humana começa na fertilização. [DISCORDA]
[15] Christopher_George - RESPONDE A [14]: >Mas o feto humano **depende** de um humano para tornar-se humano  Eu quis dizer que "uma coisa é uma coisa e outra coisa é outra coisa" um feto de um cachorro não vai virar um humano porque é o feto de um cachorro e não de um humano   > Um bebê que nasce com algum tipo de deficiência que impede ele de ter conciência, mas mesmo assim cresce e se desenvolve, ele é um ser humano ou não?   Que tipo de situação seria essa? Se puder citar uma situação que isso de fato tenha acontecido e não seja só uma situação hipotética aí eu entendo seu ponto, porque até onde eu sei todo ser humano é capaz de desenvolver consciência, até uma pessoa em estado vegetativo pode recobrar consciência   >Então, o ponto é justamente que você e nem ninguém consegue dizer em qual momento a vida começa, em exatamente o que pode ser começa a ser, isso em um sentido filosófico e ético, porque segundo a biologia a vida humana começa na fertilização.   Vida é diferente de consciência, que como eu já disse, seria aquilo que **na** **minha** **visão**  provém de um **ponto** **específico** que seria aquele ponto do desenvolvimento do cérebro que eu já falei.  >o ponto é justamente que você e nem ninguém consegue dizer em qual momento a vida começa    Você se lembra de como era a "vida" antes de você nascer? Então, a vida começa a partir do nascimento [CONCORDA]
[16] Mark_Warren - RESPONDE A [15]: Tratando do exemplo da pessoa em estado vegetativo que pode recobrar a consciência, a vida dessa pessoa somente vale algo porque ela em algum momento foi consciente? O que seria essa consciência? Uma pessoa com grave retardo é menos consciente? Se for ele vale menos então?  >Você se lembra de como era a "vida" antes de você nascer? Então, a vida começa a partir do nascimento   Se eu não lembro não aconteceu? Eu não lembro do meu nascimento, eu não nasci? [DISCORDA]
[17] Christopher_George - RESPONDE A [16]: >Tratando do exemplo da pessoa em estado vegetativo que pode recobrar a consciência, a vida dessa pessoa somente vale algo porque ela em algum momento foi consciente? O que seria essa consciência? Uma pessoa com grave retardo é menos consciente? Se for ele vale menos então?  Não. Aquilo que dá a pessoa a capacidade de ser um indivíduo(?). Se ela é capaz de pensar por si, creio eu que não(não sei se na neurologia seria classificado diferente). Não, porque aquela pessoa já está viva, criou memórias, laços, etc. Então ela já **é** por isso "vale" mais do que o **poder** **ser**    >Se eu não lembro não aconteceu? Eu não lembro do meu nascimento, eu não nasci?   Você não se lembra mas os outros se lembram por você, antes de você nascer não há como **ninguém** se lembrar. Só depois do nascimento. [CONCORDA]
[18] Mark_Warren - RESPONDE A [13]: O que seria essa tal consciência humana que define o ser humano? Cérebros humanos não são iguais e do mesmo modo a consciência de cada indivíduo é única, o bebê é menos consciente que o adulto, seria ele menos humano? Ele se enquadraria no pode ser, outros nem isso conseguem, alguém que nasce com forte retardo não poderá nunca ser consciente em um nível similar a vasta maioria dos outros humanos. [OUTROS]
[19] Christopher_George - RESPONDE A [18]: >O que seria essa tal consciência humana que define o ser humano?   __"A consciência ou consciez é uma qualidade da mente, considerando abranger qualificações tais como subjetividade, autoconsciência, senciência, sapiência, e a capacidade de perceber a relação entre si e um ambiente. É um assunto muito pesquisado na filosofia da mente, na psicologia, neurologia e ciência cognitiva."__ -Wikipédia   Edit: Tô com preguiça de **tentar** definir consciência e eu tbm não sou o maior estudioso de filosofia    >Ele se enquadraria no pode ser, outros nem isso conseguem, alguém que nasce com forte retardo não poderá nunca ser consciente em um nível similar a vasta maioria dos outros humanos.  Mas essa pessoa ainda teria consciência, não? [OUTROS]
[20] Mark_Warren - RESPONDE A [11]: Se nasce um bebê sem cérebro, esse não seria humano? Tu esqueceu de falar também que apartir da semana 24 ele pode sobreviver fora do útero com ajuda de humanos adultos, assim como qualquer outro bebê, que bebê sobrevive sozinho fora do útero? [OUTROS]
[21] Christopher_George - RESPONDE A [20]: >Se nasce um bebê sem cérebro, esse não seria humano?   Em momento algum eu disse que não seria, além do mais ele já estaria vivo então não seria um feto e sim um **bebê** **humano**   >que bebê sobrevive sozinho fora do útero?   Não entendi como isso é relevante ao assunto já que eu estava falando sobre o feto e não sobre o bebê, se ele já **nasceu** então já está **vivo** [OUTROS]
[22] Mark_Warren - RESPONDE A [21]: De que modo o embrião/feto não são seres vivos? Porque toda essa distinção entre o feto e o bebê, da forma que tu fala parece que o canal vaginal transforma o feto em algo completamente novo, o bebê 1 dia antes de nascer, ainda no ventre é menos do que ele é quando nasce? O que de tão mágico ocorre nesse processo? [DISCORDA]
[23] Christopher_George - RESPONDE A [22]: >De que modo o embrião/feto não são seres vivos?   Se você tivesse uma esposa e ela estivesse e você precisasse escolher entre salvar ela ou o bebê, quem você salvaria? Quem é mais importante pra você? O bebê que não nasceu e não vai sofrer pelo aborto ou sua esposa?   >Por que toda essa distinção entre o feto e o bebê?    Não era o intuito original do post?   >Da forma que tu fala parece que o canal vaginal transforma o feto em algo completamente novo, o bebê 1 dia antes de nascer, ainda no ventre é menos do que ele é quando nasce? O que de tão mágico ocorre nesse processo?    Não, porque esse período de 1 dia é **insignificante** se comparado à semanas ou meses antes dele **possivelmente** nascer [CONCORDA]
[24] Mark_Warren - RESPONDE A [23]: >Se você tivesse uma esposa e ela estivesse e você precisasse escolher entre salvar ela ou o bebê, quem você salvaria? Quem é mais importante pra você? O bebê que não nasceu e não vai sofrer pelo aborto ou sua esposa?  Você não respondeu a pergunta, porque o feto/embrião não é um ser vivo? A tua resposta não importa na consideração moral do aborto, podemos fazer o mesmo agora com o bebê, se eu tivesse um bebê no ventre da minha esposa eu estaria ok em matar várias pessoas por ele, e isso não nos diz que é ok matar aquelas pessoas, apenas que eu valorizo mais meu bebê do que estas outras vidas, o fato de eu ser contra aborto não quer dizer que eu valorizo cada pessoa igualmente, apenas quer dizer que eu valorizo o embrião/feto mais que algumas pessoas.  >Não era o intuito original do post?  Não  >Não, porque esse período de 1 dia é **insignificante** se comparado à semanas ou meses antes dele **possivelmente** nascer  Porque o bebê quando nasce tem valor e antes não? Porque eu não posso matar o bebê? Porque essa linha arbitrária de valorização da vida humana? [DISCORDA]
[25] Christopher_George - RESPONDE A [24]: >Você não respondeu a pergunta, porque o feto/embrião não é um ser vivo? A tua resposta não importa na consideração moral do aborto, podemos fazer o mesmo agora com o bebê, se eu tivesse um bebê no ventre da minha esposa eu estaria ok em matar várias pessoas por ele, e isso não nos diz que é ok matar aquelas pessoas, apenas que eu valorizo mais meu bebê do que estas outras vidas.  Até um certo ponto ele não seria, por não ter consciência, aí volta naquele período de desenvolvimento do cérebro onde o aborto antes desse período seria "correto(na minha visão)".   >O fato de eu ser contra aborto não quer dizer que eu valorizo cada pessoa igualmente, apenas quer dizer que eu valorizo o embrião/feto mais que algumas pessoas.   É você quem vai cuidar do bebê se ele nascer? Se não então, em que a pessoa escolher abortar ou não afeta sua vida? A **possível** vida de um bebê — que poderia ser cheia de adversidades por ter vindo de uma gravidez não planejada, por exemplo — vale mais que a vida de alguém que já está vivo?   >Não era o intuito original do post?  >Não  Como não?? O post pergunta se o aborto é aceitável, se ele for aceitável é inevitável que essa distinção entre o feto e o bebê ocorra   >Porque o bebê quando nasce tem valor e antes não? Porque eu não posso matar o bebê? Porque essa linha arbitrária de valorização da vida humana?  Porque quando ele nasce não tem como ele "desnascer" diferente de um feto que não nasceu. Porque é um **bebê**. Não sei, está perguntando a pessoa errada. Você mesmo admitiu valorizar a vida do seu bebê — que não teria nascido ainda — mais do que a vida de outras pessoas, deveria estar perguntado isso a si mesmo. [CONCORDA]
[26] Mark_Warren - RESPONDE A [25]: >Até um certo ponto ele não seria, por não ter consciência, aí volta naquele período de desenvolvimento do cérebro onde o aborto antes desse período seria "correto(na minha visão)".   Um ser pode ser vivo e não ter consciência, bactérias são seres vivos sem consciência, humanos também podem estar vivos e não ter consciência, como em um coma ou enquanto dormem, se tu somente se importa com seres conscientes e a potencialidade de consciência é um não fator pra ti então não haveria problemas em matar pessoas em coma.  >É você quem vai cuidar do bebê se ele nascer? Se não então, em que a pessoa escolher abortar ou não afeta sua vida? A **possível** vida de um bebê — que poderia ser cheia de adversidades por ter vindo de uma gravidez não planejada, por exemplo — vale mais que a vida de alguém que já está vivo?  O aborto não afeta apenas a mãe, afeta o pai, outros familiares e claro, o bebê. A existência e a forma como outras pessoas são tratadas me afeta,por isso eu também sou contra escravidão mesmo nunca tido sido escravizado ou dono de escravos, se a vida de alguém vale menos por possivelmente ser cheia de adversidades então matemos todos os deficientes e minorias, na verdade porque não matamos todo mundo, dai ninguém sofre, de novo, não é questão de valer mais ou menos, é questão de valer algo, se a mãe não quer o bebê que o coloque para adoção ou entregue a familiares que o queram, lhe garanto que adultos que viveram em orfanatos estão gratos por estarem vivos, eles não pensam que suas vidas são um erro.  >Como não?? O post pergunta se o aborto é aceitável, se ele for aceitável é inevitável que essa distinção entre o feto e o bebê ocorra  Não é, eu mesmo estou desafiando essa distinção enquanto converso contigo, tu também pode argumentar que não há distinção entre feto e bebê enquanto argumenta a favor do aborto, mas dai tu teria que ser a favor da morte de bebês.  >Porque quando ele nasce não tem como ele "desnascer" diferente de um feto que não nasceu. Porque é um **bebê**. Não sei, está perguntando a pessoa errada. Você mesmo admitiu valorizar a vida do seu bebê — que não teria nascido ainda — mais do que a vida de outras pessoas, deveria estar perguntado isso a si mesmo.  Tu ainda não me respondeu porque nascer é tão imporante, qual a magia do nascer? feto=fodace, bebê=valioso porque? Eu valorizo a vida deste suposto bebê ainda não nascido mais do que a vida de outras pessoas pelo mesmo motivo que tu valoriza mais a tua mãe do que outras pessoas, porque a tua mãe vale mais pra ti do que pra mim? [DISCORDA]
[27] Christopher_George - RESPONDE A [26]: >Um ser pode ser vivo e não ter consciência, bactérias são seres vivos sem consciência, humanos também podem estar vivos e não ter consciência, como em um coma ou enquanto dormem, se tu somente se importa com seres conscientes e a potencialidade de consciência é um não fator pra ti então não haveria problemas em matar pessoas em coma.  Isso é totalmente diferente, pois essas pessoas em coma já estiveram conscientes em algum determinado momento, muito diferente de um feto que nunca esteve consciente. Quanto as bactérias, sim elas estão vivas mesmo sem "consciência(porque elas ainda conseguem tomar decisões)" mas é claro que algo já ter tido/ter ou não consciência diminui o "valor" daquela vida.   >O aborto não afeta apenas a mãe, afeta o pai, outros familiares e claro, o bebê.   Que bebê? É um **possível** bebê e não um bebê, além disso você quer mesmo comparar o **impacto** que a gravidez tem na **mãe** com o impacto que tem nas pessoas ao redor? É igual a comparar as adversidades que um pobre e um rico enfrentam na vida mesmo que o outro também sofra, é nítido quem passa por mais merda   >A existência e a forma como outras pessoas são tratadas me afeta,por isso eu também sou contra escravidão mesmo nunca tido sido escravizado ou dono de escravos, se a vida de alguém vale menos por possivelmente ser cheia de adversidades então matemos todos os deficientes e minorias, na verdade porque não matamos todo mundo, dai ninguém sofre, de novo, não é questão de valer mais ou menos, é questão de valer algo, se a mãe não quer o bebê que o coloque para adoção ou entregue a familiares que o queiram, lhe garanto que adultos que viveram em orfanatos estão gratos por estarem vivos, eles não pensam que suas vidas são um erro.   Quando que eu disse que a vida de alguém vale menos por ser cheia de adversidades? Não trata-se de valer menos trata-se de diminuir o sofrimento, se seu filho fosse nascer com alguma deficiência que impactaria **toda** a vida dele, mas você tivesse a escolha de abortar, você deixaria ele viver uma vida **muito** **mais** **difícil** só porque sim?? Ao invés de abortar e impedir uma pessoa que teria uma vida cheia de adversidades, É ÓBVIO que qualquer pessoa passa por adversidades mas nem se compara o quão mais fácil seria a vida de alguém sem deficiências. "Se a mãe não quer o bebê entregue…" e quem garante que esse bebê teria uma boa vida? Você prefere deixar na mão do destino pra saber se esse bebê vai viver em um lar amável e acolhedor ou viver um inferno na terra? É claro que existem muitos pai horríveis por aí mas entre apostar na sorte daquela criança ter uma boa infância ou não ter infância nenhuma eu prefiro a segunda opção(óbvio que eu tô falando do caso de aborto e não pra matar a criança já viva só porque ela vive com pais horríveis). "Gratos por estarem vivos" sim, sim. Você falou com **TODAS** as pessoas que cresceram em orfanatos pra saber disso, né?    >Não é, eu mesmo estou desafiando essa distinção enquanto converso contigo, tu também pode argumentar que não há distinção entre feto e bebê enquanto argumenta a favor do aborto, mas dai tu teria que ser a favor da morte de bebês.   Como não há distinção entre feto e bebê? Só pelo fato do feto só conseguir sobreviver fora do útero depois de um determinado tempo já comprova que há uma distinção.    >Tu ainda não me respondeu porque nascer é tão imporante, qual a magia do nascer? feto=fodace, bebê=valioso porque? Eu valorizo a vida deste suposto bebê ainda não nascido mais do que a vida de outras pessoas pelo mesmo motivo que tu valoriza mais a tua mãe do que outras pessoas, porque a tua mãe vale mais pra ti do que pra mim?  Porque ele não pode "desnascer", eu já falei. Porque o bebê já nasceu, simples. Porque eu já vivi com minha mãe, portanto já criei memórias, laços, etc. Depois que esse possível bebê nascesse você continuaria se importando com ele? Em algum momento esse bebê vai crescer e virar outro adulto e o ciclo vai se repetir e então, você vai se importar mais com outro possível bebê ou com o adulto que antes de ser um adulto era um bebê? [CONCORDA]
[28] Katrina_Novak - RESPONDE A [23]: Em que momento começa a ter vida? Qual seria o problema de uma pessoa dizer que pode matar um bebê já nascido de 2 meses pois ainda não considera que tenha vida significante para que n seja assassinado? Qual o critério que usamos se tudo é subjetivo? [OUTROS]
[29] Christopher_George - RESPONDE A [28]: >Em que momento começa a ter vida? Qual seria o problema de uma pessoa dizer que pode matar um bebê já nascido de 2 meses pois ainda não considera que tenha vida significante para que n seja assassinado? Qual o critério que usamos se tudo é subjetivo?  Eu já respondi, a partir do ponto em que o bebê pode desenvolver uma "consciência". O bebê já nasceu não? Então, ele não pode "desnascer", portanto seria um assassinato. Acho que se basear naquilo que já **"é"** é um bom critério. [CONCORDA]
[30] Katrina_Novak - RESPONDE A [29]: Pq é a consciência que faz ele ser um ser humano? Se outras pessoas acharem que é em etapas posteriores que é considerado um ser humano, vc concordaria que elas possam matar quando ele só tem a consciência? [OUTROS]
[31] Christopher_George - RESPONDE A [30]: >Pq é a consciência que faz ele ser um ser humano? Se outras pessoas acharem que é em etapas posteriores que é considerado um ser humano, vc concordaria que elas possam matar quando ele só tem a consciência?  Porque a consciência humana é resultante de um cérebro humano. Um grupo de pessoas "achar" algo não torna aquilo verdadeiro, por isso existe a ciência para provar as coisas ao invés de se basear em achismos. [OUTROS]
[32] Katrina_Novak - RESPONDE A [31]: Ok, quis me referir quando as pessoas pensam no momento em que há vida, algumas pensam quando tem consciência, outras quando primeiro respiram ao nascer... [OUTROS]
[33] Matthew_Davenport - RESPONDE A [9]: Bem colocado. [DISCORDA]
[34] Matthew_Davenport - RESPONDE A [8]: A forma de vida humana e sua capacidade de se colocar no lugar dos outros além tambem de sua evolução que superou a de qualquer outro ser vivo fez de nós superiores a os animais que por sua vez sao superiores as plantas, que por sua vez sao superiores a micro-organismos, nao atoa reinamos sobre todos esses e os unicos capazes de escolher causar intencionalmente sofrimento ou não. Somos superiores. [DISCORDA]
[35] Matthew_Davenport - RESPONDE A [8]: Nao é ainda tudo bem pensar assim mas vai ser a menos que alguem se meta no curso e interrompa por pura vontade peopria de nao querer ter, mas ninguem obriga voce a ser a mae do filho. Existe ama de leite e ala para recem nascidos e depois existe lar de crianças e jovens. [DISCORDA]
[36] Jamie_Hayes - RESPONDE A [8]: >algumas vertentes que tb levam em consideração que o feto deve ser considerado vivo apartir do momento que sente dor(que tem receptores nervosos)   Tu tirou isso dá onde? Então pessoas com analgesia congênita não são seres vivos, já que não sentem dor... [DISCORDA]
[37] Matthew_Davenport - RESPONDE A [36]: Sao seres vivos mas n tem problma ir la e causar danos neles ja que eles nao vao sentir machucar. É isso que eu li? N vou rir pelo respeito e pela seriedade que o camarada ali da a nossa discussão. Bem colocado seu ponto, amigo. [OUTROS]
[38] Shawn_Bell - RESPONDE A [7]: é por isso que essa discussão nunca vai ter fim, somente a fecundação não é uma vida, vai da opinião de cada pessoa, pra mim só é vida qnd tem uma sinapse mental, antes disso só é um conglomerado de celulas tal qual uma verruga, e a nispse mental só vem la pra frente na gestação     e toda a parte de parir no minimo, de que adianta nascer e não ser nutrido corretamente e só ter uma vida de sofrimento, isso é muito mais egoismo [CONCORDA]
[39] David_Fuller - RESPONDE A [38]: >e toda a parte de parir no mínimo, de que adianta nascer e não ser nutrido corretamente e só ter uma vida de sofrimento, isso é muito mais egoísmo   Não importa como você define quais são as circunstancias o bebe vai nascer. Isso é irrelevante. Você não tem direito de "ser feliz", mas você tem direito a pp que lhe concede direito a vida e imputa ao seus pais a responsabilidade pelo seu bem-estar até você ser capaz de cuidar de si mesmo. Isso não é definido porque isso faz da vida das pessoas mais fácil, como seria o caso da felicidade, mas sim pq é basicamente um aspecto fundamental da maneira como a sociedade funciona. Por isso é uma medida ética. [OUTROS]
[40] Austin_Lee - RESPONDE A [7]: Te parir no mínimo, tu tá ligado que não é uma parada simples né? São 9 meses, transformações hormonais, psicológicas e físicas, a responsabilidade legal depois que a criança nasce, a incapacidade de trabalhar durante meses... Pra muita gente isso significa acabar com a vida delas. [OUTROS]
[41] Matthew_Davenport - RESPONDE A [40]: Entao voce transou sabendo o que pode acontecer e depois n pode pagar o preço mesmo NAO sendo obrigado a cuidar da criança depois? A responsabilidade de tratar da sua saúde é unica e exclusivamente sua tendo bons habitos evitando comer porcaria industriais, tomando agua e se exercitando, tudo isso é barato ou de graça (pasme existe comida saudável barata), inclusive ajuda no psicológico. E isso tudo voce tambem pode fazer sem estar gravida ta?   Existe leis e auxilio pra mãe solteira ou gestante, ou a pensao ou apoio do pai (sim eu sei que o pai pode nao ajudar em nada ao descobrir que vc ta grávida mas entao tu deu pra um malandro irresponsável igual a voce ainda por cima??) Escolhas e consequências... aí n quer pagar o preço entao vai interferir na liberdade dessa nova vida? depois de 9 meses é tchau pra criança pq alguem com certeza vai cuidar dela melhor do que esses humanos que o geraram.  Dizer que 9 meses pode (do ponto de vista da pessoa) "acabar com a vida" dela, isso configura mais como consequência dos próprios atos e achar que vai acabar com a sua vida me parece mais uma incompreensão da propria irresponsabilidade de uma pessoa que so fez sexo sabendo do 0,1% de risco de gravidez independente do metodo contraceptivo usado (afinal só vazectomia é 0% de risco). Aí depois quer matar uma vida em curso e desenvolvimento. Egoísmo, luxo. Voce é superior a alguem da sua especie pra interferir no curso dele? Mesmo que esse indivíduo ainda nao esta completamente formado e independente? Mesmo que esse indivíduo vai depender unica e exclusivamente de você por 9 meses?? Se voce acha isso, voce não pode ser considerado um humano normal, é um dissimulado, mau, que acha que suas escolhas podem estar decidindo a vida ou morte de um de sua espécie (ai mas n é gente ainda! ngm era gente caso nossas maes metessem o dedo no nosso desenvolvimento nos primeiros estágios de formação e desenvolvimento).  Uma namorada minha um dia ao descobrir gravidez disse que queria abortar pq n queria ter filho apenas pq n aguentaria psicológicamente igualzinho voce descreveu ai "ia acabar com a vida dela" e eu tb nunca quis pq tb vai "acabar com a minha" mas eu disse que ela parisse e me desse a criança e que nunca mais olhasse na minha cara e que não precisaria ajudar em nada e acompanhar em nada, uma criança nao merece deixar de nascer por luxo de uma safada egoista que gosta de dar mas depois simplesmente enlouquece ao saber de uma gravidez. Eu jamais quis ter um filho mas ao saber de uma gravidez eu sei que essa responsabilidade é minha então eu assumo essa porra. Nao mataria entao facilitei pra ela e salvei o futuro do meu filho. Quem pariu vive bem hoje e tem sua vida da forma que sempre quis: "sem filhos". E deve estar tranquila da forma que sempre quis.  Abortar é puramente por Egoísmo e luxo na maior parte dos casos e matar uma vida por isso era pra ser crime. A maior parte que aborta so vive sempre pensando no momento e em como se sente, chegando a um ponto que da pra chamar de irresponsabilidade. [DISCORDA]
[42] Adam_Walsh - RESPONDE A [7]: Então comer frutas é o mesmo que derrubar uma floresta. [CONCORDA]
[43] Matthew_Davenport - RESPONDE A [42]: Nessa analogia, comer fruta é o mesmo que jogar fora o esperma ao gozar onde nao é fértil (fora do utero) e as sementes dentro da fruta sao como os espermatozoides no saco do homem, sozinhos n fazem nada, tem que cair (gozar dentro) e entrar na terra (fecundar), aí começa o crescimento. Semente sozinha n faz nada.  Mas eu queria te responder com mais ignorância que: "sim, amigo é a mesma coisa" porem que n sei pq, mas eu queria colocar algum entendimento na sua cabeça. Por favor nao se ofenda, eu so fiz isso pq no fundo eu gosto de você assim como gosto de todos conterrâneos da mesma espécie, inclusive aqueles em formação. [DISCORDA]
[44] Adam_Walsh - RESPONDE A [43]: Mano, acho que você não sabe a diferença entre um zigoto e um esperma então. Se um óvulo fecundado é uma pessoa (o que obviamente não é verdade) então uma fruta, que é algo que foi fecundado também, é uma árvore. [CONCORDA]
[45] Matthew_Davenport - RESPONDE A [44]: Não é uma pessoa, é o início de uma é ja esta determinado o produto final e o processo seguirá sozinho. A fecundação da fruta é diferente mesmo da do ser humano, ocorre antes mas nessa analogia eu comparei a fecundação do óvulo com a entrada da semente na terra e nao necessariamente o que é a fecundação de cada uma das espécies e que elas sao iguais. [DISCORDA]
[46] Adam_Walsh - RESPONDE A [45]: Acho que essa diferença é deliberadamente arbitrária nesse caso. Acho que obviamente um potencial para ser uma pessoa não é uma pessoa, assim como uma fruta não é uma árvore. Se uma pessoa não quer ter um feto dentro dela, não vejo o problema em expurgar a coisa se desejado, ainda mais se é pelo bem social e bem-estar da pessoa. [CONCORDA]
[47] Matthew_Davenport - RESPONDE A [46]: Bem estar da pessoa ? Ela nao consegue esperar 9 meses e depois nunca mais olhar pra criança na vida dela se ela quiser? Eu entendo que tem casos de abuso e tudo mais mas na maioria das vezes  a maior parte das pessoas que defendem o aborto é só gente que quer na real nao ter o filho caso aconteça o inesperado. Se vc n quer ter filhos nao transe pq ate de camisinha ou tomando AC  tem 0,1% de chance. Depois pede pra legalizar o aborto pq se n legalizar vai no ilegal mesmo e corre risco. Quer falar de bem estar da pessoa e o bem estar da vida que ja ta em curso? O bem estar dela esta acima da decisao de interromper o curso de uma vida? Imagina as árvores nao aguentarem uma fruta pendurada nelas somente até essa merda cair e por elas nao queriam ter fruta e por causa disso nunca deixar dar fruta nenhuma alegando "meu tronco minhas regras, meu bem estar" o que custa a arvore deixar a fruta ali so ate cair e poder evoluir sozinha ??? Isso porque seres humanos sao muito mais complexos que que árvores alem de que a arvore se reproduz sozinha e os seres humanos nao, uma fruta que caiu ja ta dando curso a uma nova arvore mas um curso de vida humano só é dado quando ocorre a fecundação do óvulo. [DISCORDA]
[48] Adam_Walsh - RESPONDE A [47]: Ok, mas olha só: A pessoa não quer ter essa vida em curso dentro dela, então ela não é obrigada. É um monte de células sem consciência ou capacidade de existir sozinho, tipo um tumor. A árvore não tem capacidade de decidir, mas ela faz o que está no seu DNA. A gente tem a capacidade de decidir, então podemos decidir o que a gente pode fazer com nossos corpos.   Eu não posso forçar você a doar sangue ou um órgão mesmo que isso interrompa uma vida que está em curso. A pessoa pode transar o quanto ela quiser, ela não é obrigada a servir de incubadora humana. Eu só quero que mais pessoas estejam seguras, felizes e saudáveis, e tudo indica que a legalização do aborto faz da sociedade um lugar melhor para todos. Como já é óbvio, qualquer argumento contra é só religioso e se agarra em dogmas e definições impossíveis de se comprovar, então não podem ser levadas a sério. [CONCORDA]
[49] Kyle_Andrade - RESPONDE A [1]: Esperma não é feto. Meu Deus cada burrice que se le na Internet. [DISCORDA]
[50] Shawn_Bell - RESPONDE A [49]: Sério mesmo que são coisas diferentes???   Vc é muito foda em interpretação de texto mesmo [CONCORDA]
[51] Kyle_Andrade - RESPONDE A [50]: Amigo, sua comparação só pode ser feita e aceita por pessoas com menos de 80 de QI. [DISCORDA]
[52] Jeffrey_Dunn - RESPONDE A [51]: Só pessoas de QI baixo acreditam em QI [OUTROS]
[53] Kyle_Andrade - RESPONDE A [52]: Hahahahahaahahahaahaahahahahahahahahahaha [OUTROS]
[54] Jared_Murray - RESPONDE A [1]: So se ninguém para vc ninguém conseguir dar um bom argumento contra matar outra pessoa sem ser religioso. Um feto em fase intermediária já tem consciência e sente dor. [DISCORDA]
[55] Shawn_Bell - RESPONDE A [54]: Ai que ta a questão, feto não é uma pessoa, é so um conglomerado de células sem nenhuma sinapse mental ate um estágio avançado da concepção [CONCORDA]
[56] Jared_Murray - RESPONDE A [55]: De onde vc tirou isso, tem fontes, e onde é esse estado avançado da concepção? O que define ele em termos biológicos?  É exatamente isso que separa o feto de uma pessoa?   Essas perguntas são importantes de serem respondidas se vc tem tanta certeza assim. Eu considero que a partir de um sistema de nervoso que o feto possa sentir dor já é uma violação ética grave.  Sou a favor até os 3 meses por isso. [DISCORDA]
[57] Mark_Warren - RESPONDE A [1]: Não é questão de vida, se as pessoas fossem contra qualquer morte morreriam de fome, a questão é vida HUMANA, espermatozoides não são humanos. [DISCORDA]
[58] Shawn_Bell - RESPONDE A [57]: Feto tbm não é vida humana [CONCORDA]
[59] Mark_Warren - RESPONDE A [58]: Porque não? [OUTROS]
[60] Shawn_Bell - RESPONDE A [59]: É tão humano qnt um espermatozóide, são apenas estágios distintos com potencial de virar um humano no futuro [CONCORDA]
[61] Katrina_Novak - RESPONDE A [60]: Qual o problema de eu dizer que im bebê nascido de 3 meses não é humano pois ainda está se desenvolvendo? [DISCORDA]
[62] Mark_Warren - RESPONDE A [60]: O espermatozoide é apenas um recorte de DNA de seu criador, uma espécie de clone com apenas 23 cromossomos, ele apenas transporta o material genético, no momento da fecundação essa amostra genética se junta ao óvulo da mulher e ai começa o processo de desenvolvimento humano, o anterior não tem nem a base genética necessária para garantir humanidade, seguindo a tua mesma lógica tudo que forma o humano seria humano, cada célula do teu corpo é um humano e vale tanto quanto um embrião, uma definição completamente inútil pois não define nada, as células do teu corpo são humanas porque pertencem a um humano, o embrião é humano pois não pode ser qualquer outra coisa. [DISCORDA]
[63] Shawn_Bell - RESPONDE A [62]: Um óvulo fecundado tbm é apenas um recorte de 2 DNAs, tal qual um espermatozóide não é um humano, um feto fecundado tbm não é, essa é a grande questão, definir a partir de que momento existe vida e pode ser considerado um ser humano   Na minha concepção seria na primeira sinapse cerebral, mas já levantaram a questão dos acéfalos, e sinceramente não sei como decidir nesse caso, é um corpo humano, mas não sei dizer se basta para ser considerado ser humano   Se vc acredita que na fecundação já seja um ser humano, então vc deveria ter um repúdio gigantesco por clínicas de fertilização in vitro, pq vários embriões são fecundados ali, e depois seleciona os que tem mais chances de dar certo, ou seja, vários "seres humanos" são mortos e descartados [CONCORDA]
[64] Beverly_Black - RESPONDE A [1]: Prazer, ninguém. :) [DISCORDA]
[65] Shawn_Bell - RESPONDE A [64]: E cade o argumento sem religião? [OUTROS]
[66] Beverly_Black - RESPONDE A [65]: Procura aí que você acha nessa mesma página. Não tem religião pq não sou religioso.   100% baseado em analogia e lógica. [OUTROS]
[67] Beverly_Black - RESPONDE A [1]: E se o pai da criança quiser ter seu filho? O pai é sempre colocado de fora nessa questão.  O pai e mãe cada um tem 50% de responsabilidade sobre a existência da gravidez e do filho mas a opinião do pai é sempre nem comentada nessas ocasiões. [DISCORDA]
[68] Walter_Rosario - RESPONDE A [1]: Já ouviu falar de criação de família, continuidade do patrimônio, continuidade da raça humana, fora a ética e moral que não estão ligadas a religião mas como você deve ser um adolescente de 15 anos você não consegue fazer essa distinção assim como acha que um feto e um esperma são a mesma coisa [DISCORDA]
### MENSAGEM ATUAL:
Shawn_Bell - RESPONDE A [68]: Quem tá querendo abortar, não ta em busca da criação de uma família, ou de continuidade do patrimônio (bem o contrário na vdd), e o mundo está sofrendo de superpopulação, não estamos precisando sair procriando igual doído não   Ética e moral variam de tempos em tempos, não existe uma ética e moral correta, isso é pessoal de cada 1  E por último, não sei da onde vc tirou que esperma e feto são a mesma coisa, mas o fato é que os espermatozóides tem uma vida útil de 3 dias, e se toda "vida" que pode virar um humano é sagrada, todos ja cometemos genocídio
### MENSAGEM DE REFERÊNCIA:
Eu acho que a pessoa que é contra o aborto está usando uma lógica moralista e religiosa para justificar sua posição, mas isso não é uma razão objetiva para negar o direito das mulheres de tomar decisões sobre seu próprio corpo. Além disso, se considerarmos o feto como vida, então teríamos que aplicar a mesma lógica para outras questões, como a masturbação, que poderia ser considerada um genocídio se considerarmos a vida do feto como uma vida humana. Isso mostra que a lógica usada para justificar a proibição do aborto é inconsistente e não pode ser aplicada de forma justa e igualitária
Classifique o posicionamento da **mensagem atual** com relação à **mensagem de referência**. Leve em consideração todo o contexto.
"""
    }
]
)

print(completion.choices[0].message.content)