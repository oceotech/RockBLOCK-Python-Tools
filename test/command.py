from unittest import TestCase
from imp import load_source
from shlex import split
from utils import captured_output

command_module = load_source('command', 'bin/rockblock')


class CommandTestCase(TestCase):
    def test_valid_commands(self):
        parser = command_module.parser

        valid_commands = [
            'rockblock send imei user pass "Hello, World"',
            'rockblock send imei user pass "Hello, World" --data-format=raw',
            'rockblock send imei user pass 48656c6c6f2c20576f726c6421 --data-format=hex',
            'rockblock send imei user pass SGVsbG8sIFdvcmxkIQ== --data-format=base64',
            'rockblock listen console 0.0.0.0 80',
            'rockblock listen csv 0.0.0.0 80 path/to/file.csv',
            'rockblock listen mqtt 0.0.0.0 80 localhost 1883 my/mqtt/topic --mqtt-user=user --mqtt-pass=pass --mqtt-qos=0',
        ]

        for command in valid_commands:
            try:
                parser.parse_args(split(command)[1:])
            except:
                self.fail('Exception parsing valid command: {}'.format(command))

    def test_invalid_commands(self):
        parser = command_module.parser

        invalid_commands = [
            'rockblock send imei user pass',
            'rockblock send imei user pass "Hello, World" --data-format=foo',
            'rockblock send imei user pass 48656c6c6f2c20576f726c6421y --data-format=hex',
            'rockblock send imei user pass SGVsbG8sIFdvcmxkIQ= --data-format=base64',
            'rockblock listen console 0.0.0.0',
            'rockblock listen console 0.0.0.0 animal',
            'rockblock listen csv 0.0.0.0 80',
            'rockblock listen mqtt 0.0.0.0 80 localhost 1883 my/mqtt/topic --mqtt-qos=9',
            'rockblock listen mqtt 0.0.0.0 80 localhost 1883',
        ]

        for command in invalid_commands:
            try:
                with captured_output():
                    parser.parse_args(split(command)[1:])

                self.fail('No exception parsing invalid command: {}'.format(command))
            except:
                pass
