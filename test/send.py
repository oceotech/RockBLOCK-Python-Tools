from unittest import TestCase
from requests import put
from rockblock_tools import send
from rockblock_tools.exception import ApiException

FAKE_API_ENDPOINT = 'http://fake_api:1080/'


class SendTestCase(TestCase):
    def test_send(self):
        # Reset the fake API server
        put('{}reset'.format(FAKE_API_ENDPOINT))

        # Create an expectation
        put('{}expectation'.format(FAKE_API_ENDPOINT), json={
            'httpRequest': {
                'method': 'POST',
                'path': '/',
            },
            'httpResponse': {
                'statusCode': 200,
                'headers': {
                    'Content-Type': ['text/plain']
                },
                'body': 'OK,12345678'
            },
        })

        # Dispatch message
        imei = 'test-imei'
        username = 'joe'
        password = 'bl0gs'
        data = 'Hello, World!'
        data_hex = '48656c6c6f2c20576f726c6421'

        mt_id = send(imei, username, password, data, FAKE_API_ENDPOINT)

        # Check the mtId
        self.assertEqual(12345678, mt_id)

        # Verify the request received was what we expected
        response = put('{}verify'.format(FAKE_API_ENDPOINT), json={
            'httpRequest': {
                'method': 'POST',
                'path': '/',
                'headers': {
                    'Content-Type': ['application/x-www-form-urlencoded']
                },
                'body': {
                    'type': 'PARAMETERS',
                    'parameters': {
                        'imei': [imei],
                        'username': [username],
                        'password': [password],
                        'data': [data_hex],
                    },
                },
            },
            'times': {
                'atLeast': 1,
                'atMost': 1,
            },
        })

        self.assertEqual(202, response.status_code, 'Received expected status code from API submission assertation')

    def test_send_error(self):
        # Reset the fake API server
        put('{}reset'.format(FAKE_API_ENDPOINT))

        # Create an expectation
        put('{}expectation'.format(FAKE_API_ENDPOINT), json={
            'httpRequest': {
                'method': 'POST',
                'path': '/',
            },
            'httpResponse': {
                'statusCode': 200,
                'headers': {
                    'Content-Type': ['text/plain']
                },
                'body': 'FAILED,50,Random error'
            },
        })

        # Dispatch message
        imei = 'test-imei'
        username = 'joe'
        password = 'bl0gs'
        data = 'Hello, World!'
        data_hex = '48656c6c6f2c20576f726c6421'

        with self.assertRaises(ApiException) as context_manager:
            send(imei, username, password, data, FAKE_API_ENDPOINT)

        exception = context_manager.exception

        self.assertEqual('RockBLOCK API gave error code 50: Random error', str(exception))

        # Verify the request received was what we expected
        response = put('{}verify'.format(FAKE_API_ENDPOINT), json={
            'httpRequest': {
                'method': 'POST',
                'path': '/',
                'headers': {
                    'Content-Type': ['application/x-www-form-urlencoded']
                },
                'body': {
                    'type': 'PARAMETERS',
                    'parameters': {
                        'imei': [imei],
                        'username': [username],
                        'password': [password],
                        'data': [data_hex],
                    },
                },
            },
            'times': {
                'atLeast': 1,
                'atMost': 1,
            },
        })

        self.assertEqual(202, response.status_code, 'Received expected status code from API submission assertation')
