#importando o pacote do flask responsável pela aplicação back-end
# jsonify para montar a resposta do servidor como json
#request para capturar as solicitações ao servidor
from flask import Flask, jsonify, request
# metodo para validar a origem das requisições
from flask_cors import CORS

# construindo a aplicação flask
app = Flask(__name__)
CORS(app) 

# definito o endereco (rota) de acesso
@app.route('/')
def servidor_rodando():
    return jsonify([
        {"mensagem": "Servido rodando com sucesso"},
    ])

@app.route('/cliente')
def lista_cliente():
    lista = [
                {"id": 1, "nome": "Maria"}
                , {"id": 2, "nome": "Jose"}
             ]
    return jsonify(lista)

#iniciando a aplicação
if __name__ == "__main__":
    app.run(debug=True)
