# importando bibliotecas
import numpy as np
import joblib
from flask import Flask, request, jsonify, render_template

# definindo objeto Flask
app = Flask(__name__, template_folder='.')

# função para verificar se a pessoa tem ou não diabetes
def previsao_diabetes(lista_valores_formulario):
    prever = np.array(lista_valores_formulario).reshape(1,8)
    modelo_salvo = joblib.load('../algoritmo-ml/modelo_diabetes.sav')
    resultado = modelo_salvo.predict(prever)
    return resultado[0]

@app.route('/formulario')
def home():
    return render_template('formulario.html')

@app.route('/resultado', methods=['POST'])
def resultado():
    if request.method == 'POST':
        lista_formulario = request.form.to_dict()
        lista_formulario = list(lista_formulario.values())
        lista_formulario = list(map(float, lista_formulario))
        resultado = previsao_diabetes(lista_formulario)
        if int(resultado) == 1:
            previsao = 'Possui Diabetes'
        else:
            previsao = 'Não possui Diabetes'

        # retorna o resultado para a pagina html
        return render_template("resultado.html", previsao = previsao)

if __name__ == "__main__":
    app.run(debug = True)