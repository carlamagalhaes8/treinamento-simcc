import pandas as pd

from dao.banco import Connection
from model.pesquisador import Pesquisador


def consultar_pesquisadores():

    sql = """
        SELECT
            pesquisadores_id,
            lattes_id,
            nome
        FROM pesquisadores;
    """

    with Connection() as conn:
        registros = conn.select(sql)

    df = pd.DataFrame(
        registros,
        columns=[
            "pesquisadores_id",
            "lattes_id",
            "nome"
        ]
    )

    pesquisadores = []

    for _, dados in df.iterrows():

        pesquisador = Pesquisador(
            pesquisadores_id=dados["pesquisadores_id"],
            lattes_id=dados["lattes_id"],
            nome=dados["nome"]
        )

        pesquisadores.append(
            pesquisador.gerar_json()
        )

    return pesquisadores


def consultar_pesquisador(pesquisadores_id):

    sql = """
        SELECT
            pesquisadores_id,
            lattes_id,
            nome
        FROM pesquisadores
        WHERE pesquisadores_id = %s;
    """

    with Connection() as conn:
        registro = conn.select(
            sql,
            [pesquisadores_id]
        )

    if len(registro) == 0:
        return None

    pesquisador = Pesquisador(
        pesquisadores_id=registro[0][0],
        lattes_id=registro[0][1],
        nome=registro[0][2]
    )

    return pesquisador.gerar_json()


def inserir_pesquisador(dados):

    sql = """
        INSERT INTO pesquisadores (
            lattes_id,
            nome
        )
        VALUES (%s, %s);
    """

    parametros = [
        dados["lattes_id"],
        dados["nome"]
    ]

    with Connection() as conn:
        conn.exec(sql, parametros)


def atualizar_pesquisador(
        pesquisadores_id,
        dados
):

    sql = """
        UPDATE pesquisadores
        SET
            lattes_id = %s,
            nome = %s
        WHERE pesquisadores_id = %s;
    """

    parametros = [
        dados["lattes_id"],
        dados["nome"],
        pesquisadores_id
    ]

    with Connection() as conn:
        conn.exec(
            sql,
            parametros
        )


def alterar_pesquisador(
        pesquisadores_id,
        dados
):

    pesquisador = consultar_pesquisador(
        pesquisadores_id
    )

    if pesquisador is None:
        return

    lattes_id = dados.get(
        "lattes_id",
        pesquisador["lattes_id"]
    )

    nome = dados.get(
        "nome",
        pesquisador["nome"]
    )

    sql = """
        UPDATE pesquisadores
        SET
            lattes_id = %s,
            nome = %s
        WHERE pesquisadores_id = %s;
    """

    parametros = [
        lattes_id,
        nome,
        pesquisadores_id
    ]

    with Connection() as conn:
        conn.exec(
            sql,
            parametros
        )


def excluir_pesquisador(
        pesquisadores_id
):

    sql = """
        DELETE FROM pesquisadores
        WHERE pesquisadores_id = %s;
    """

    with Connection() as conn:
        conn.exec(
            sql,
            [pesquisadores_id]
        )