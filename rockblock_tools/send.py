from binascii import hexlify
from requests import post
from rockblock_tools.exception import ApiException
from six import string_types

ROCKBLOCK_API_ENDPOINT = 'https://rockblock.rock7.com/rockblock/MT'


def send(imei, username, password, data, url=ROCKBLOCK_API_ENDPOINT):
    response = post(url, data={
        'imei': imei,
        'username': username,
        'password': password,
        'data': hexlify(data if not isinstance(data, string_types) else data.encode('utf-8')),
    })

    response_segments = response.text.split(',')

    status = response_segments[0]

    if status == 'OK':
        # Success, return mtId
        return int(response_segments[1])
    elif status == 'FAILED':
        try:
            error_code = int(response_segments[1])
            error_message = response_segments[2]
        except:
            raise RockBLOCKException('Could not parse API failed response')

        raise ApiException(error_code, error_message)
    else:
        raise RockBLOCKException('API returned unknown response format')
