from flask import Blueprint, jsonify, request
from dao import dao_pesquisadores

rest_pesquisador = Blueprint("rest_pesquisador", __name__)


@rest_pesquisador.route("/pesquisador", methods=["GET"])
def consultar_pesquisadores():

    lista = dao_pesquisadores.consultar_pesquisadores()

    return jsonify(lista), 200


@rest_pesquisador.route("/pesquisador/<pesquisadores_id>", methods=["GET"])
def consultar_pesquisador(pesquisadores_id):

    pesquisador = dao_pesquisadores.consultar_pesquisador(
        pesquisadores_id
    )

    if pesquisador is None:
        return jsonify(
            {"erro": "Pesquisador não encontrado"}
        ), 404

    return jsonify(pesquisador), 200


@rest_pesquisador.route("/pesquisador", methods=["POST"])
def inserir_pesquisador():

    dados = request.get_json()

    print("Dados recebidos:", dados)

    dao_pesquisadores.inserir_pesquisador(dados)

    return jsonify({
        "mensagem": "Pesquisador inserido com sucesso"
    }), 201


@rest_pesquisador.route("/pesquisador/<pesquisadores_id>", methods=["PUT"])
def atualizar_pesquisador(pesquisadores_id):

    dados = request.get_json()

    dao_pesquisadores.atualizar_pesquisador(
        pesquisadores_id,
        dados
    )

    return jsonify(
        {"mensagem": "Pesquisador atualizado com sucesso"}
    ), 200


@rest_pesquisador.route("/pesquisador/<pesquisadores_id>", methods=["PATCH"])
def alterar_pesquisador(pesquisadores_id):

    dados = request.get_json()

    dao_pesquisadores.alterar_pesquisador(
        pesquisadores_id,
        dados
    )

    return jsonify(
        {"mensagem": "Pesquisador alterado com sucesso"}
    ), 200


@rest_pesquisador.route("/pesquisador/<pesquisadores_id>", methods=["DELETE"])
def excluir_pesquisador(pesquisadores_id):

    dao_pesquisadores.excluir_pesquisador(
        pesquisadores_id
    )

    return jsonify(
        {"mensagem": "Pesquisador removido com sucesso"}
    ), 200