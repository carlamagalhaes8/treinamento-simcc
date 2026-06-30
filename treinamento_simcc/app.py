from flask import Flask, request, jsonify
from flask_cors import CORS

from rag.rag_service import buscar_similaridade

app = Flask(__name__)

# Permite requisições do frontend Next.js
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

@app.route("/ask", methods=["POST"])
def ask():

    data = request.get_json()

    question = data.get("question", "").strip()

    if not question:
        return jsonify([])

    resultado = buscar_similaridade(question)

    return jsonify(resultado)


if __name__ == "__main__":
    app.run(debug=True)