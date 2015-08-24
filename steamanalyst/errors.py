from steamanalyst import settings


class SteamAnalystAPIKeyNotPresent(Exception):
    def __init__(self):
        message = 'The {} environment variable was not set.'
        formatted = message.format(settings.API_KEY_NAME)
        super(SteamAnalystAPIKeyNotPresent, self).__init__(formatted)


class SteamAnalystUnauthorized(Exception):
    def __init__(self):
        message = 'Unable to authenticate with the Steam Analyst API.'
        super(SteamAnalystUnauthorized, self).__init__(message)


class SteamAnalystUnexpectedResponseFormat(Exception):
    def __init__(self):
        message = 'Response was not in the anticipated format.'
        super(SteamAnalystUnexpectedResponseFormat, self).__init__(message)


class SteamAnalystUnexpectedStatusCode(Exception):
    def __init__(self, status_code):
        message = 'The API endpoint returned an unexpected status code: {}.'
        formatted = message.format(status_code)
        super(SteamAnalystUnexpectedStatusCode, self).__init__(formatted)


class NotImplemented(Exception):
    def __init__(self):
        message = 'This method has not been implemented.'
        super(NotImplemented, self).__init__(message)
