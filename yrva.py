import flask
from flask import Flask
from flask import request
import datetime
import json


app = Flask(__name__)
"""
listy pro messages a linky do CSV
"""
messages = [json.loads('{"msg":"Ahoj"}'), json.loads('{"msg":"Cau, jak se mas?"}'), json.loads('{"msg":"Dobre co ty?"}'), json.loads('{"msg":"Taky dobry, pojd si psat"}'), json.loads('{"msg":"Ok"}')]
links = [json.loads('{"href":"https://localhost/restapi/v1/message","rel":"all","type":"GET"}'),
         json.loads('{"href":"https://localhost/restapi/v1/message/<id>","rel":"_self","type":"GET"}'),
         json.loads('{"href":"https://localhost/restapi/v1/message/<id>","rel":"_self","type":"DELETE"}'),
         json.loads('{"href":"https://localhost/restapi/v1/message/poslat","rel":"_self","type":"POST"}'),
         json.loads('{"href":"https://localhost/restapi/v1/message/upravit","rel":"_self","type":"PUT"}'),
         json.loads('{"href":"https://localhost/links","rel":"adressess","type":"GET"}')]



@app.route('/restapi/v1/message', methods=['GET'])
def zobrazit_zpravy():
    """
    Metoda pro vypsani vsech zprav v JSON.

    :return: vsechny zpravy v JSON
    """
    return messages


@app.route('/restapi/v1/message/<id>', methods=['GET'])
def zobrazit_jednu_zpravu(id):
    """
    Metoda pro vypsani zpravy podle <id>.

    :param id: cislo zpravy
    :return: vypsani zpravy v JSON
    """
    return messages[int(id) - 1]


@app.route('/restapi/v1/message/<id>', methods=['DELETE'])
def smazat_zpravu(id):
    """
    metoda pro smazani zpravy.

    :param id: id zpravy pro smazani.
    :return: smazana zprava.
    """
    messages.pop(int(id) - 1)
    return f"Smazal jste zprávu s id {id}"


@app.route('/restapi/v1/message/poslat', methods=['POST'])
def poslat_zpravu():
    """
    Metoda pro vytvoreni zpravy.

    :param msg: Hodnota zpravy.
    :return: vypise se na obrazovku ze metoda prosla
    """

    try:
        messages.append(json.loads('{"msg":"' + str(request.json["msg"]) + '"}'))
    except IndexError:
        flask.abort(404)
    flask.jsonify(set=True)
    return "Poslal jste zprávu: " + request.json["msg"]


@app.route('/restapi/v1/message/upravit', methods=['PUT'])
def upravit_zpravu():
    """
    Metoda pro upraveni zpravy
    :param id: id zzpravy kterou upravuju
    :param msg: upravena zprava
    :return:
    """

    try:
        messages[int(request.json["id"]) - 1] = json.loads('{"msg":"' + str(request.json["msg"]) + '"}')
    except IndexError:
        flask.abort(404)
    flask.jsonify(set=True)
    return "Upravil jste zprávu s id " + request.json["id"]

@app.route('/links', methods=['GET'])
def linky():
    """
    Metoda co vrati linky
    :return: pole s linkama
    """
    return links


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
