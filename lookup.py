# coding=utf-8
import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")
adresses = []

while True:
    # Esperar alguma mensagem
    req = socket.recv_json()
    if req['type'] == "POST" and req['route'] == "Adress/":
        # "Limpa" a requisição e só salva Adress e name
        del req['type']
        del req['route']
        adresses.append(req)
        res = {"code": "400"}
        socket.send_json(res)
        print("Adress of: %s. Saved!" % req['name'])
    # Se estiver pedindo um endereço
    elif req['type'] == "GET" and req['route'] == "Adress/":
        res = ""
        # Checa se existe o endereço solicitado
        for item in adresses:
            # Se existir enviar res vira o json com adress e name e codigo 400 (sucesso)
            if item['name'] == req['name']:
                res = item
                res['code'] = "400"
                break
            # Se não, envia o codigo 200 (erro)
            else:
                res = {"code": "200"}

        socket.send_json(res)
        print("Adress of: %s. Sent!" % req['name'])

    print(adresses)
