import pandas as pd
from dao.banco import Connection
from model.producao import Producao


def consultar_producoes():

    sql = """
        SELECT
            producoes_id,
            pesquisadores_id,
            issn,
            nomeartigo,
            anoartigo
        FROM producoes;
    """

    with Connection() as conn:
        registros = conn.select(sql)

    df = pd.DataFrame(
        registros,
        columns=[
            "producoes_id",
            "pesquisadores_id",
            "issn",
            "nomeartigo",
            "anoartigo"
        ]
    )

    lista = []

    for _, dados in df.iterrows():

        producao = Producao(
            producoes_id=dados["producoes_id"],
            pesquisadores_id=dados["pesquisadores_id"],
            issn=dados["issn"],
            nomeartigo=dados["nomeartigo"],
            anoartigo=dados["anoartigo"]
        )

        lista.append(producao.gerar_json())

    return lista


def consultar_producao(producoes_id):

    sql = """
        SELECT
            producoes_id,
            pesquisadores_id,
            issn,
            nomeartigo,
            anoartigo
        FROM producoes
        WHERE producoes_id = %s;
    """

    with Connection() as conn:
        registro = conn.select(sql, [producoes_id])

    if not registro:
        return None

    p = registro[0]

    producao = Producao(
        producoes_id=p[0],
        pesquisadores_id=p[1],
        issn=p[2],
        nomeartigo=p[3],
        anoartigo=p[4]
    )

    return producao.gerar_json()


def inserir_producao(dados):

    sql = """
        INSERT INTO producoes (
            pesquisadores_id,
            issn,
            nomeartigo,
            anoartigo
        )
        VALUES (%s, %s, %s, %s);
    """

    valores = [
        dados["pesquisadores_id"],
        dados["issn"],
        dados["nomeartigo"],
        dados["anoartigo"]
    ]

    with Connection() as conn:
        conn.exec(sql, valores)


def atualizar_producao(producoes_id, dados):

    sql = """
        UPDATE producoes
        SET
            pesquisadores_id = %s,
            issn = %s,
            nomeartigo = %s,
            anoartigo = %s
        WHERE producoes_id = %s;
    """

    valores = [
        dados["pesquisadores_id"],
        dados["issn"],
        dados["nomeartigo"],
        dados["anoartigo"],
        producoes_id
    ]

    with Connection() as conn:
        conn.exec(sql, valores)


def alterar_producao(producoes_id, dados):

    atual = consultar_producao(producoes_id)

    if atual is None:
        return

    pesquisadores_id = dados.get("pesquisadores_id", atual["pesquisadores_id"])
    issn = dados.get("issn", atual["issn"])
    nomeartigo = dados.get("nomeartigo", atual["nomeartigo"])
    anoartigo = dados.get("anoartigo", atual["anoartigo"])

    sql = """
        UPDATE producoes
        SET
            pesquisadores_id = %s,
            issn = %s,
            nomeartigo = %s,
            anoartigo = %s
        WHERE producoes_id = %s;
    """

    valores = [
        pesquisadores_id,
        issn,
        nomeartigo,
        anoartigo,
        producoes_id
    ]

    with Connection() as conn:
        conn.exec(sql, valores)


def excluir_producao(producoes_id):

    sql = """
        DELETE FROM producoes
        WHERE producoes_id = %s;
    """

    with Connection() as conn:
        conn.exec(sql, [producoes_id])