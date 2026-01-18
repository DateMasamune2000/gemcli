import requests
import json

class GeminiConnection:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.headers = {'x-goog-api-key': self.key, 'Content-Type': 'application/json'}
        self.history = []

    def prompt(self, p):
        self.history.append({"role":"user","parts":[{"text":p}]})
        jsondata = {"contents": self.history}
        r = requests.post(self.url, data=json.dumps(jsondata), headers=self.headers)
        if r.status_code != 200:
            print(r.text)
        txt = json.loads(r.text)['candidates'][0]['content']['parts'][0]
        self.history.append({"role":"model","parts":[{"text":txt["text"]}]})
        return txt

