from dotenv import load_dotenv

load_dotenv()

from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vetor = embeddings.embed_query(
    "arboviroses"
)

print(len(vetor))
print(vetor[:5])