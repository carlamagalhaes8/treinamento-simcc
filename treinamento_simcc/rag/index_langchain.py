from dotenv import load_dotenv
load_dotenv()

import psycopg2
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

# embeddings
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

# conectar no MESMO banco
conn = psycopg2.connect(
    host="localhost",
    database="BD_PESQUISADOR",
    user="postgres",
    password="qualquer_uma",
    port="5437"
)

cursor = conn.cursor()

cursor.execute("""
    SELECT nomeartigo
    FROM producoes
    WHERE nomeartigo IS NOT NULL
""")

rows = cursor.fetchall()
docs = [r[0] for r in rows]

print(f"📄 Total de documentos encontrados: {len(docs)}")

vector_store.add_texts(docs)

print("✅ Indexação concluída com sucesso!")