#!/usr/bin/env python

from argparse import ArgumentParser
from rockblock_tools import send, listen
from rockblock_tools.exception import RockBLOCKException, ApiException
from rockblock_tools.formatter import ConsoleFormatter, CSVFormatter, MQTTFormatter
from sys import exit

parser = ArgumentParser(description='Send and receive messages from the RockBLOCK web services.')
subparsers = parser.add_subparsers(title='commands', help='Available commands', dest='command')

send_parser = subparsers.add_parser('send', help='Send a message to a RockBLOCK')
send_parser.add_argument('imei', type=str, help='RockBLOCK IMEI number')
send_parser.add_argument('username', type=str, help='Your RockBLOCK username')
send_parser.add_argument('password', type=str, help='Your RockBLOCK password')
send_parser.add_argument('data', type=str, help='The data you want to send')
send_parser.add_argument('--data-format', type=str, default='raw', choices=['raw', 'hex', 'base64'], help='What format is your data in?')


def send_command(args):
    decoder = {
        'raw': lambda d: d,
        'hex': lambda d: d.decode('hex'),
        'base64': lambda d: d.decode('base64'),
    }

    data = decoder[args.data_format](args.data)

    try:
        send(args.imei, args.username, args.password, data)
    except RockBLOCKException as e:
        print(e)
        exit(1)

    exit(0)


listen_parser = subparsers.add_parser('listen', help='Listen to web hooks from a RockBLOCK')
listen_subparsers = listen_parser.add_subparsers(title='formats', help='Available formats', dest='format')


def listen_command(args):
    formatter = {
        'console': ConsoleFormatter,
        'csv': CSVFormatter,
        'mqtt': MQTTFormatter,
    }[args.format](args)

    try:
        listen(args.host, args.port, formatter)
    finally:
        formatter.close()


listen_console_parser = listen_subparsers.add_parser('console')
listen_console_parser.add_argument('host', type=str, help='The host to listen on, e.g. 0.0.0.0')
listen_console_parser.add_argument('port', type=str, help='The port to listen on, e.g. 80')
listen_console_parser.add_argument('--data-format', type=str, default='raw', choices=['raw', 'hex', 'base64'], help='What format should the data be encoded in?')

listen_csv_parser = listen_subparsers.add_parser('csv')
listen_csv_parser.add_argument('host', type=str, help='The hostname to listen on, e.g. localhost')
listen_csv_parser.add_argument('port', type=str, help='The port to listen on, e.g. 80')
listen_csv_parser.add_argument('csv_file', type=str, help='The CSV file to write messages to')
listen_csv_parser.add_argument('--data-format', type=str, default='raw', choices=['raw', 'hex', 'base64'], help='What format should the data be encoded in?')

listen_mqtt_parser = listen_subparsers.add_parser('mqtt')
listen_mqtt_parser.add_argument('host', type=str, help='The hostname to listen on, e.g. localhost')
listen_mqtt_parser.add_argument('port', type=str, help='The port to listen on, e.g. 80')
listen_mqtt_parser.add_argument('mqtt_host', type=str, help='The MQTT broker host')
listen_mqtt_parser.add_argument('mqtt_port', type=int, help='The MQTT broker port')
listen_mqtt_parser.add_argument('mqtt_topic', type=str, help='The MQTT topic to publish to')
listen_mqtt_parser.add_argument('--mqtt-user', type=str, default=None, help='The username for the MQTT broker')
listen_mqtt_parser.add_argument('--mqtt-pass', type=str, default=None, help='The password for the MQTT broker')
listen_mqtt_parser.add_argument('--mqtt-qos', type=int, default=0, choices=[0, 1, 2], help='The password for the MQTT broker')
listen_mqtt_parser.add_argument('--data-format', type=str, default='raw', choices=['raw', 'hex', 'base64'], help='What format should the data be encoded in?')


def main():
    args = parser.parse_args()

    if 'send' == args.command:
        send_command(args)
    elif 'listen' == args.command:
        listen_command(args)
