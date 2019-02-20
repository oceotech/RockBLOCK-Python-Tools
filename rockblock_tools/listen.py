from flask import Flask, request
from datetime import datetime
import logging


class InboundMessage:
    def __init__(self, payload):
        self.iridium_latitude = float(payload['iridium_latitude'])
        self.iridium_longitude = float(payload['iridium_longitude'])
        self.device_type = payload['device_type']
        self.transmit_time = datetime.strptime(payload['transmit_time'], '%d-%m-%y %H:%M:%S')
        self.momsn = int(payload['momsn'])
        self.imei = payload['imei']
        self.serial = payload['serial']
        self.data = payload['data'].decode('hex')
        self.iridium_cep = float(payload['iridium_cep'])


def create_view_func(callback):
    def view_func():
        callback(InboundMessage(request.form))

        return '', 200

    return view_func


def listen(host, port, callback):
    app = Flask('webhook-listener')
    app.config['ENV'] = 'production'

    logger = logging.getLogger('werkzeug')
    logger.disabled = True

    view_func = create_view_func(callback)

    app.add_url_rule('/', 'webhook', view_func=view_func, methods=['POST'])

    app.run(host=host, port=port)
