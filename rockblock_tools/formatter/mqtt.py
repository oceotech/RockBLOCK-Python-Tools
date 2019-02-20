from paho.mqtt.publish import single as mqtt_single


class MQTTFormatter:
    def __init__(self, args):
        self.args = args

    def __call__(self, message):
        payload = {
            'Iridium Latitude': message.iridium_latitude,
            'Iridium Longitude': message.iridium_longitude,
            'Device Type': message.device_type,
            'Transmit Time': message.transmit_time,
            'MOMSN': message.momsn,
            'IMEI': message.imei,
            'Serial': message.serial,
            'Data': message.data if self.args.data_format == 'raw' else message.data.encode(self.args.data_format),
            'Iridium CEP': message.iridium_cep,
        }

        auth = None

        if self.args.mqtt_user is not None:
            auth = {'username': self.args.mqtt_user}

            if self.args.mqtt_pass is not None:
                auth['password'] = self.args.mqtt_pass

        mqtt_single(
            topic=self.args.mqtt_topic,
            payload=payload,
            qos=self.args.mqtt_qos,
            hostname=self.args.mqtt_host,
            port=self.args.mqtt_port,
            auth=auth
        )

    def close(self):
        pass
