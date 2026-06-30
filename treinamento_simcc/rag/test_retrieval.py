from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

CONNECTION_STRING = "postgresql+psycopg2://postgres:qualquer_uma@localhost:5437/BD_PESQUISADOR"

vector_store = PGVector(
    connection=CONNECTION_STRING,
    embeddings=embeddings,
    collection_name="producoes",
    use_jsonb=True
)

print("✅ Vector store conectado com sucesso!")

query = "arboviroses"

results = vector_store.similarity_search(query, k=5)

print("\n🔎 RESULTADOS:\n")

for doc in results:
    print("-----")
    print(doc.page_content)