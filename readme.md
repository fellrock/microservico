Demo Analise Sentimento
===

Ambiente
-----

```sh
mkdir Ambientes
cd Ambientes
python3 -m venv analise_sentimento
cd analise_sentimento
source bin/activate
mv <pasta>/Tweets_Mg.csv .
pip install jupyter scikit-learn flask pandas
jupyter-notebook
ctrl+c
deactivate
exit
```

----

API
----

```sh
python api.py
curl http://localhost:5000/
curl http://localhost:5000/predict -XPOST --data '{"Text": "mensagem a ser analisada"}'
```

----

