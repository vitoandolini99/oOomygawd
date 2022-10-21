# oOomygawd

# Stajny.py
/restapi/v1/message - METODA GET: Vypíše všechny zprávy
/restapi/v1/message/id - METODA GET: Vypíše zprávu se zadaným id
/restapi/v1/message/id - METODA DELETE: Vymaže zprávu se zadaným id
/restapi/v1/message/zprava - METODA POST: Uloží novou zprávu
/restapi/v1/message/id/zprava - METODA PUT: Upraví zprávu podle id

# yrva.py
/restapi/v1/message - s metodou GET vypíše všechny existující zprávy
/restapi/v1/message/id - s metodou GET vypíše konkrétní zprávu dle zadaného id
/restapi/v1/message/id - s metodou DELETE vymaže konkrétní zprávu dle zadaného id
/restapi/v1/message/poslat - s metodou POST přidá novou zprávu (v soapui dole v textovém poli ve formátu json [atribut "msg"])
/restapi/v1/message/upravit - s metodou PUT upraví konktrétní zprávu (v soapui dole v textovém poli ve formátu json [atributy "id" a "msg"])
