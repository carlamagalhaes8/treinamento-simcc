from dotenv import load_dotenv
load_dotenv()

from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

CONNECTION = "postgresql+psycopg2://postgres:qualquer_uma@localhost:5437/BD_PESQUISADOR"

COLLECTION = "producoes_v2"

vector_store = PGVector(
    embeddings=embeddings,
    connection=CONNECTION,
    collection_name=COLLECTION,
    use_jsonb=True
)