from requests import post

ROCKBLOCK_API_ENDPOINT = 'https://rockblock.rock7.com/rockblock/MT'


def send(imei, username, password, data, url=ROCKBLOCK_API_ENDPOINT):
    result = post(url, data={
        'imei': imei,
        'username': username,
        'password': password,
        'data': data,
    })
