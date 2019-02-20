class ConsoleFormatter:
    def __init__(self, args):
        self.data_format = args.data_format

    def __call__(self, message):
        print('''
---------- MESSAGE ----------
Iridium Latitude  {}
Iridium Longitude {}
Device Type       {}
Transmit Time     {}
MOMSN             {}
IMEI              {}
Serial            {}
Data              {}
Iridium CEP       {}
-----------------------------
'''.format(
        message.iridium_latitude,
        message.iridium_longitude,
        message.device_type,
        message.transmit_time,
        message.momsn,
        message.imei,
        message.serial,
        message.data if self.data_format == 'raw' else message.data.encode(self.data_format),
        message.iridium_cep
    ))

    def close(self):
        pass
