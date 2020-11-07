from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)
pipe = load('pipeline.joblib')

@app.route('/')
def home():
    return '''
    Olá Mundo! 
    /predict (POST): {"Text": "mensagem a ser analisada"}
    '''
@app.route('/predict',methods=['POST'])
def predict():

    requisicao = request.get_json(force=True)
    tweet = requisicao['Text']
    resultado = pipe.predict([tweet])[0]
    return jsonify({'Sentimento': resultado})

if __name__ == "__main__":
    app.run(debug=True)