
from flask import Flask, request, render_template
import re
import string
import nltk
from nltk.corpus import stopwords
from clases import variablesInicio
import random
from clases.estadistica import  listaVariables

nltk.download('stopwords')

app = Flask(__name__, template_folder="templates")


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/estadistica', methods=['GET'])
def estadistica():
    return listaVariables


@app.route('/prediccion/<string:modelo>/<string:dataset>', methods=['GET'])
def prediction(modelo, dataset):
    return render_template('prediction.html', modelo=modelo, dataset=dataset)


@app.route('/estadisticas', methods=['GET'])
def estadisticasHTML():
    dat = listaVariables
    return render_template('estadisticas.html', dataset="estadisticas", datos=dat)


@app.route('/contactos', methods=['GET'])
def contactos():
    dat = listaVariables
    return render_template('contacts.html', dataset="contactos", datos=dat)


@app.route('/prediccion/rf/sintomas/graficasSintomas', methods=['GET'])
def graficasSintomas():
    return render_template('graficas.html', dataset="graficasSintomas")


@app.route('/prediccion/rf/recomendaciones/graficasRecomendaciones', methods=['GET'])
def graficasRecomendaciones():
    return render_template('graficas.html', dataset="graficasRecomendaciones")


@app.route('/clasificadorModelo', methods=['POST'])
def clasificador():

    try:
        body = request.get_json()
        validarRequestBody(body)
        variablesInicio.definirVariablesModelo(body['modelo'], body['dataset'])

        entrada = procesarEntrada(body['entrada'])
        x_entry = vectorizarEntrada(entrada)
        y_predict = clasificar(x_entry)
        columnas, salidas = obtenerResultados(y_predict)

        res = {"columnas": columnas, "entrada": body['entrada'],
               "salidaModelo": y_predict[0].tolist(), "prediccion": salidas}

        return {"codigo": 0, "mensaje": "Operacion Realizada con éxito", "Respuesta": res}
    except ValueError as e:
        return {"codigo": random.randint(1, 100), "mensaje": str(e), "body": None}


def validarRequestBody(body):

    if body:
        if "modelo" not in body or body['modelo'] == '':
            raise ValueError('Se debe especificar el modelo')
        if "dataset" not in body or body['dataset'] == '':
            raise ValueError('se debe especificar el dataset')
        if "entrada" not in body or body['entrada'] == '':
            raise ValueError('se debe incluir una entrada')

        if body['modelo'] not in variablesInicio.modelos:
            raise ValueError(
                'se debe especificar un modelo válido: Randosm Forest(rf) o Support vector Machine(svm)')
        if body['dataset'] not in variablesInicio.datasets:
            raise ValueError(
                'se debe especificar un dataset válido: sintomas o recomendaciones')
    else:
        raise ValueError('No existe un body Request')


def procesarEntrada(entrada):
    entrada_limpia = clean_text(entrada)
    entrada_separada_espacios = entrada_limpia.split(" ")
    important_words = filter(lambda x: x not in stopwords.words(
        'spanish'), entrada_separada_espacios)
    entry = " ".join(list(important_words))
    return entry


def vectorizarEntrada(entrada):
    entrada_vectorizada = variablesInicio.vectorizador.transform(
        [entrada]).toarray()
    return entrada_vectorizada


def clasificar(entrada_vectorizada):
    y_predict = variablesInicio.clasificador.predict(entrada_vectorizada)
    return y_predict


def obtenerResultados(y_predict):
    columnas = []
    salida = []

    for columna, valor in zip(variablesInicio.y_test, y_predict[0]):
        columnas.append(columna)
        if valor == 1:
            salida.append(columna)

    return columnas, salida


def clean_text(text):
    text = str(text)
    text = text.lower()
    text = re.sub('á', 'a', text)
    text = re.sub('é', 'e', text)
    text = re.sub('í', 'i', text)
    text = re.sub('ó', 'o', text)
    text = re.sub('ú', 'u', text)
    text = re.sub('\[.*?¿\]\%', ' ', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('\w*\d\w*', '', text)
    text = re.sub('[‘’“”…«»]', '', text)
    text = re.sub('\n', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub('[^a-zA-Z]', ' ', text)
    return text


if __name__ == '__main__':
    app.run(debug=True)
