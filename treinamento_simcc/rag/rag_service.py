from dao.dao_producoes import preparar_textos_para_rag
from rag.vector_store import vector_store

indexado = False


def carregar_base():
    global indexado

    if indexado:
        return

    textos, metadados = preparar_textos_para_rag()

    print(f"Quantidade de textos: {len(textos)}")

    vector_store.add_texts(
        texts=textos,
        metadatas=metadados
    )

    print("Base indexada com sucesso!")

    indexado = True


def buscar_similaridade(query):

    carregar_base()

    resultados = vector_store.similarity_search_with_score(
        query=query,
        k=5
    )

    resposta = []

    for doc, score in resultados:

        metadata = doc.metadata or {}

        print(metadata)

        # Ignora documentos antigos sem metadados
        if not metadata.get("titulo"):
            continue

        resposta.append({
            "titulo": metadata.get("titulo"),
            "pesquisador": metadata.get("pesquisador"),
            "ano": metadata.get("ano"),
            "similaridade": round(float(score), 4)
        })

    return resposta