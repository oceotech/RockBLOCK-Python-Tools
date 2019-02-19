from requests import post
from rockblock_tools.exception import ApiException

ROCKBLOCK_API_ENDPOINT = 'https://rockblock.rock7.com/rockblock/MT'


def send(imei, username, password, data, url=ROCKBLOCK_API_ENDPOINT):
    response = post(url, data={
        'imei': imei,
        'username': username,
        'password': password,
        'data': data.encode('hex'),
    })

    response_segments = response.content.split(',')

    status = response_segments[0]

    if status == 'OK':
        # Success
        return
    elif status == 'FAILED':
        try:
            error_code = int(response_segments[1])
            error_message = response_segments[2]
        except:
            raise RockBLOCKException('Could not parse API failed response')

        raise ApiException(error_code, error_message)
    else:
        raise RockBLOCKException('API returned unknown response format')
