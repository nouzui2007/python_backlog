import requests

from config import config



class Base:
    headers = {}
    params = {}

    def __init__(self):
        self.params['apiKey'] = config['backlog']['apiKey']

    def getBaseUrl(self):
        return config['backlog']['baseUrl']

    def getProjectKey(self):
        return config['backlog']['projectKey']

    def get(self, uri):
        print(self.params)
        response = requests.get(
            f'{self.getBaseUrl()}{uri}', headers=self.headers, params=self.params)
        return response.json()

    def patch(self, uri):
        response = requests.patch(
            f'{self.getBaseUrl()}{uri}', params=self.params, headers=self.headers)
        return response.json()


class User(Base):
    list = []

    def __init__(self):
        super().__init__()
        self.list = self.get('/users')

    def findByName(self, name):
        return list(map(lambda x: {'id': x['id'], 'name': x['name']}, filter(lambda x: name in x['name'], self.list)))

class Status(Base):
    list = []

    def __init__(self):
        super().__init__()
        self.list = self.get(f'/projects/{self.getProjectKey()}/statuses')

    def findByName(self, name):
        return list(map(lambda x: {'id': x['id'], 'name': x['name']}, filter(lambda x: name in x['name'], self.list)))


class Issue(Base):
    URI = '/issues/'
    issueKey = ''

    def __init__(self, issueKey):
        super().__init__()
        self.issueKey = f'{self.getProjectKey()}-{issueKey}'

    def getURL(self):
        return self.URI + self.issueKey

    def gain(self):
        return self.get(self.getURL())

    def update(self, data):
        self.headers['Content-Type'] = 'application/x-www-form-urlencoded'
        self.params.update(data)
        return self.patch(self.getURL())
