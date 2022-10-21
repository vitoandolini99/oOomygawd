import flask
from flask import Flask
from flask import request
import datetime
import json

app = Flask(__name__)

messages = [json.loads('{"message":"cahoj"}'), json.loads('{"message":"gej"}'), json.loads('{"message":"cccc"}')]
links = [json.loads('{"href":"http://localhost:8080/restapi/message","rel":"all","type":"GET"}'),
         json.loads('{"href":"http://localhost:8080/restapi/message/<id>","rel":"_self","type":"GET"}'),
         json.loads('{"href":"http://localhost:8080/restapi/message/<id>","rel":"_self","type":"DELETE"}'),
         json.loads('{"href":"http://localhost:8080/restapi/message/create","rel":"_self","type":"POST"}'),
         json.loads('{"href":"http://localhost:8080/restapi/message/update","rel":"_self","type":"PUT"}'),
         json.loads('{"href":"http://localhost:8080/restapi/links","rel":"addresses","type":"GET"}')]


@app.route('/')
def index():
    """
    Uvodni stranka
    :return: Uvodni stranka
    """
    return 'Vitejte na serveru SPSE Jecna'


@app.route('/restapi/message', methods=['GET'])
def vypsat_vseM():
    """
    Vypis vsech zprav v JSONu
    :return: Vsechny zpravy v JSONu
    """
    return messages


@app.route('/restapi/links', methods=['GET'])
def linky():
    """
    Metoda na vypis vsech linku v JSONu
    :return: Vsechny linky v JSONu
    """
    return links


@app.route('/restapi/message/<id>', methods=['GET'])
def get_one(id):
    """
    Vypis zpravy podle id
    :param id: id zpravy
    :return: Zprava v jsonu
    """
    return messages[int(id) - 1]


@app.route('/restapi/message/<id>', methods=['DELETE'])
def delete(id):
    """
    Smazani zpravy podle id
    :param id: id zpavy
    :return: Potvrzeni o smazani zpravy
    """
    messages.pop(int(id) - 1)
    return f"Deleted {id}"


@app.route('/restapi/message/create', methods=['POST'])
def post():
    """
    Pridani zpravy pomoci rest json
    :return: Potvrzeni provedeni operace
    """
    try:
        messages.append(json.loads('{"message":"' + str(request.json['msg']) + '"}'))
    except IndexError:
        flask.abort(404)
    return flask.jsonify(set=True)


@app.route('/restapi/message/update', methods=['PUT'])
def update():
    """
    Update zpravy pomoci rest json
    :return: Potvrzeni provedeni operace
    """
    try:
        messages[int(request.json['id']) - 1] = json.loads('{"message":"' + str(request.json['msg']) + '"}')
    except IndexError:
        flask.abort(404)
    return flask.jsonify(set=True)


@app.route('/doc')
def docs():
    """
    Metoda na vypis vsech linku v HTML
    :return: vsechny linky v HTML
    """
    return "<style>h2{font-family: \"Helvetica\";" \
           "color: white;" \
           "-webkit-text-stroke: 1px black; }" \
           "body{background-image: url('https://i.kym-cdn.com/entries/icons/original/000/041/976/cover1.jpg')}</style>" \
           "" \
           "<h2>http://localhost:8080/restapi/message - Vypis vsech zprav pres GET</h1>" \
           "<h2>http://localhost:8080/restapi/message/<id> - Vypis zpravy podle id pres GET</h1>" \
           "<h2>http://localhost:8080/restapi/message/<id> - Smazani zpravy podle id pres DELETE</h1>" \
           "<h2>http://localhost:8080/restapi/message/create - Pridani zpravy pres POST pomoci REST JSON</h1>" \
           "<h2>http://localhost:8080/restapi/message/update - Update zpravy pres PUT pomoci REST JSON</h1>" \
           "<h2>http://localhost:8080/restapi/links - Vypis vsech linku pomoci GET</h1>" \
           "<h2>http://localhost:8080/doc - dokumentace.</h1>"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=False)