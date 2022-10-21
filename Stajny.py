from flask import Flask, request
import json

app = Flask(__name__)

messages = [json.loads('{"msg":"cau more"}'), json.loads('{"msg":"cs"}'), json.loads('{"msg":"wyd"}')]
links = [json.loads('{"href":"http://localhost/restapi/v1/message", "rel":"all", "type":"GET"}'),
         json.loads('{"href":"http://localhost/restapi/v1/message/<id>", "rel":"_self", "type":"GET"}'),
         json.loads('{"href":"http://localhost/restapi/v1/message/<id>", "rel":"_self", "type":"DELETE"}'),
         json.loads('{"href":"/restapi/v1/message/<msg>", "rel":"_self", "type":"POST"}'),
         json.loads('{"href":"/restapi/v1/message/<id>/<msg>", "rel":"_self", "type":"PUT"}'),
         json.loads('{"href":"http://localhost/links", "rel":"addresses", "type":"GET"}'),
         ]


@app.route('/restapi/v1/message', methods=['GET'])
def get():
    """
    Metoda odkáže na cestu ke zprávám a vypíše všechny zprávy

    :return: Vrátí zprávy
    """
    return messages


@app.route('/restapi/v1/message/<id>', methods=['GET'])
def get_item(id):
    """
    Metoda odkáže na cestu ke konkrétní zprávě podle zadaného id a vypíše ji

    :param id: id hledané zprávy
    :return: Vrátí zprávu
    """
    return messages[int(id - 1)]


@app.route('/restapi/v1/message/<id>', methods=['DELETE'])
def delete(id):
    """
    Metoda odkáže na cestu ke konkrétní zprávě podle zadaného id a vymaže ji

    :param id: id hledané zprávy
    :return: Vrátí potvrzení a vymazání zprávy
    """
    messages.pop(int(id) - 1)
    return f"Deleted {id}"


@app.route('/restapi/v1/message/<msg>', methods=['POST'])
def post(msg):
    """
    Metoda odkáže ne cestu ke zprávám a vloží zprávu zadanou uživatelem

    :param msg: Zpráva uživatele
    :return: Vrátí zprávu kterou uživatel právě napsal
    """
    messages[int(request.json['id']) - 1] = json.loads('{"message":"' + str(request.json['msg']) + '"}')
    return f"Posted {msg}"


@app.route('/restapi/v1/message/<id>/<msg>', methods=['PUT'])
def update(id, msg):
    """
    Metoda odkáže na cestu ke zprávě podle zadaného id a upraví ji na text který zadal uživatel

    :param id: id hledané zprávy
    :param msg: úprava zprávy
    :return: Vrátí id zprávy pro potvrzení
    """
    messages[int(id) - 1] = json.loads('{"msg":"' + str(msg) + '"}')
    return f"Edited {id}"


@app.route('/links', methods=['GET'])
def link():
    """
    Metoda odkáže na cestu k linkům a všechny vypíše

    :return: Vrátí všechny linky
    """
    return links


@app.route('/doc')
def docs():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h2>/restapi/v1/message - METODA GET: Vypíše všechny zprávy</h2>
    <h2>/restapi/v1/message/id - METODA GET: Vypíše zprávu se zadaným id</h2>
    <h2>/restapi/v1/message/id - METODA DELETE: Vymaže zprávu se zadaným id</h2>
    <h2>/restapi/v1/message/zprava - METODA POST: Uloží novou zprávu</h2>
    <h2>/restapi/v1/message/id/zprava - METODA PUT: Upraví zprávu podle id</h2>
</body>
</html>"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)