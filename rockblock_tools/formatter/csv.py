from __future__ import absolute_import
from csv import DictWriter


class CSVFormatter:
    def __init__(self, args):
        self.data_format = args.data_format

        self.stream = open(args.csv_file, 'w')

        self.writer = DictWriter(self.stream, [
            'Iridium Latitude',
            'Iridium Longitude',
            'Device Type',
            'Transmit Time',
            'MOMSN',
            'IMEI',
            'Serial',
            'Data',
            'Iridium CEP',
        ])

        self.writer.writeheader()

        self.stream.flush()

    def __call__(self, message):
        self.writer.writerow({
            'Iridium Latitude': message.iridium_latitude,
            'Iridium Longitude': message.iridium_longitude,
            'Device Type': message.device_type,
            'Transmit Time': message.transmit_time,
            'MOMSN': message.momsn,
            'IMEI': message.imei,
            'Serial': message.serial,
            'Data': message.data if self.data_format == 'raw' else message.data.encode(self.data_format),
            'Iridium CEP': message.iridium_cep,
        })

        self.stream.flush()

    def close(self):
        self.stream.close()
