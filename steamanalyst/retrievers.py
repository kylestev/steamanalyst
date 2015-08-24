import json
import os
import requests
from steamanalyst import errors
from steamanalyst import settings


class APIResultRetriever(object):
    def results(self):
        raise NotImplemented()


class SteamAnalystAPIResultRetriever(APIResultRetriever):
    def __init__(self):
        try:
            this.api_key = os.environ[settings.API_KEY_NAME]
        except KeyError:
            raise errors.SteamAnalystAPIKeyNotPresent()

    def _fetch_results(self):
        url = settings.STEAM_ANALYST_ENDPOINT
        r = requests.get(url, params={'key': self.api_key})
        
        if r.status_code == 403:
            raise errors.SteamAnalystUnauthorized()
        elif r.status_code != 200:
            raise errors.SteamAnalystUnexpectedStatusCode(r.status_code)
        
        parsed = r.json()
        if not 'results' in parsed.keys():
            raise errors.SteamAnalystUnexpectedResponseFormat()
        return parsed['results']

    def results(self):
        return self._fetch_results()


class LocalAPIResultRetriever(APIResultRetriever):
    def __init__(self, file_name):
        self.file_name = file_name

    def results(self):
        with open(self.file_name, 'r') as f:
            parsed = json.loads(f.read())
            if not 'results' in parsed.keys():
                raise errors.SteamAnalystUnexpectedResponseFormat()
            return parsed['results']
