from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_postgres import PGVector

# embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

CONNECTION_STRING = "postgresql+psycopg2://postgres:qualquer_uma@localhost:5437/BD_PESQUISADOR"

# vector store
vector_store = PGVector(
    connection=CONNECTION_STRING,
    embeddings=embeddings,
    collection_name="producoes",
    use_jsonb=True
)

# LLM (ChatGPT)
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# função de RAG simples
def perguntar(query):

    # 1. busca semântica
    docs = vector_store.similarity_search(query, k=5)

    contexto = "\n\n".join([d.page_content for d in docs])

    # 2. prompt
    prompt = f"""
Você é um assistente acadêmico.
Responda usando APENAS o contexto abaixo.

CONTEXTO:
{contexto}

PERGUNTA:
{query}

Responda de forma clara e objetiva.
"""

    # 3. resposta do LLM
    resposta = llm.invoke(prompt)

    return resposta.content


# teste
if __name__ == "__main__":

    while True:
        pergunta = input("\nPergunta: ")

        if pergunta.lower() in ["sair", "exit"]:
            break

        resposta = perguntar(pergunta)
        print("\nResposta:\n")
        print(resposta)