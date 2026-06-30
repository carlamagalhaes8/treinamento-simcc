from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
import psycopg2

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

conn = psycopg2.connect(
    host="localhost",
    database="BD_PESQUISADOR",
    user="postgres",
    password="qualquer_uma",
    port="5437"
)

cursor = conn.cursor()

cursor.execute("""
SELECT
    producoes_id,
    nomeartigo
FROM producoes
""")

producoes = cursor.fetchall()

print(f"Encontradas {len(producoes)} produções")

for producao_id, titulo in producoes:

    if titulo is None:
        continue

    vetor = embeddings.embed_query(titulo)

    cursor.execute("""
        UPDATE producoes
        SET embedding = %s
        WHERE producoes_id = %s
    """,
    (vetor, producao_id))

    print("Indexado:", titulo)

conn.commit()

cursor.close()
conn.close()

print("Finalizado")