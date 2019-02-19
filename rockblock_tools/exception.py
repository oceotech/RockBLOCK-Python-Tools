class RockBLOCKException(Exception):
    pass


class ApiException(RockBLOCKException):
    def __init__(self, error_code, error_message):
        super(Exception, self).__init__('RockBLOCK API gave error code {}: {}'.format(error_code, error_message))
