from flask import Blueprint, jsonify, request
from dao import dao_producoes

rest_producao = Blueprint("rest_producao", __name__)


# GET ALL
@rest_producao.route("/producao", methods=["GET"])
def consultar_producoes():

    lista = dao_producoes.consultar_producoes()
    return jsonify(lista), 200


# GET BY ID
@rest_producao.route("/producao/<producoes_id>", methods=["GET"])
def consultar_producao(producoes_id):

    producao = dao_producoes.consultar_producao(producoes_id)

    if producao is None:
        return jsonify({"erro": "Produção não encontrada"}), 404

    return jsonify(producao), 200


# POST
@rest_producao.route("/producao", methods=["POST"])
def inserir_producao():

    dados = request.get_json()

    dao_producoes.inserir_producao(dados)

    return jsonify({"mensagem": "Produção inserida com sucesso"}), 201


# PUT
@rest_producao.route("/producao/<producoes_id>", methods=["PUT"])
def atualizar_producao(producoes_id):

    dados = request.get_json()

    dao_producoes.atualizar_producao(producoes_id, dados)

    return jsonify({"mensagem": "Produção atualizada com sucesso"}), 200


# PATCH
@rest_producao.route("/producao/<producoes_id>", methods=["PATCH"])
def alterar_producao(producoes_id):

    dados = request.get_json()

    dao_producoes.alterar_producao(producoes_id, dados)

    return jsonify({"mensagem": "Produção alterada com sucesso"}), 200


# DELETE
@rest_producao.route("/producao/<producoes_id>", methods=["DELETE"])
def excluir_producao(producoes_id):

    dao_producoes.excluir_producao(producoes_id)

    return jsonify({"mensagem": "Produção removida com sucesso"}), 200

# consultar por pesquisador_id
@rest_producao.route("/producao/pesquisador/<pesquisadores_id>", methods=["GET"])
def consultar_por_pesquisador(pesquisadores_id):

    lista = dao_producoes.consultar_producoes_por_pesquisador(
        pesquisadores_id
    )

    return jsonify(lista), 200