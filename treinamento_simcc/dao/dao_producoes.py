import pandas as pd

from dao.banco import Connection


def consultar_producoes():

    sql = """
        SELECT
            p.producoes_id,
            p.pesquisadores_id,
            pe.nome AS pesquisador_nome,
            p.issn,
            p.nomeartigo,
            p.anoartigo
        FROM producoes p
        JOIN pesquisadores pe
            ON pe.pesquisadores_id = p.pesquisadores_id
        ORDER BY p.nomeartigo;
    """

    with Connection() as conn:
        registros = conn.select(sql)

    df = pd.DataFrame(
        registros,
        columns=[
            "producoes_id",
            "pesquisadores_id",
            "pesquisador_nome",
            "issn",
            "nomeartigo",
            "anoartigo"
        ]
    )

    lista = []

    for _, dados in df.iterrows():

        lista.append({
            "producoes_id": dados["producoes_id"],
            "pesquisadores_id": dados["pesquisadores_id"],
            "pesquisador_nome": dados["pesquisador_nome"],
            "issn": dados["issn"],
            "nomeartigo": dados["nomeartigo"],
            "anoartigo": dados["anoartigo"]
        })

    return lista


def preparar_textos_para_rag():

    producoes = consultar_producoes()

    textos = []
    metadados = []

    for p in producoes:

        texto = (
            f"Artigo: {p['nomeartigo']}. "
            f"Pesquisador: {p['pesquisador_nome']}. "
            f"ISSN: {p['issn']}. "
            f"Ano: {p['anoartigo']}."
        )

        textos.append(texto)

        metadados.append({
            "titulo": p["nomeartigo"],
            "pesquisador": p["pesquisador_nome"],
            "ano": p["anoartigo"],
            "producoes_id": p["producoes_id"]
        })

    return textos, metadados