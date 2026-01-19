import requests
import json

class GeminiConnection:
    def __init__(self, url, key):
        self.url = url
        self.key = key
        self.headers = {'x-goog-api-key': self.key, 'Content-Type': 'application/json'}
        self.history = []

    # Don't add to history, just prompt.
    def raw_prompt(self, p):
        jsondata = {"contents":{"role":"user","parts":[{"text":p}]}}
        txt = self._run_prompt(jsondata)

        return txt

    # Normal "chat"
    def prompt(self, p):
        self.history.append({"role":"user","parts":[{"text":p}]})
        jsondata = {"contents": self.history}

        txt = self._run_prompt(jsondata)

        self.history.append({"role":"model","parts":[{"text":txt["text"]}]})

        return txt

    # Internal, don't use this from outside
    def _run_prompt(self, jsondata):
        r = requests.post(self.url, data=json.dumps(jsondata), headers=self.headers)
        if r.status_code != 200:
            print(r.text)

        txt = json.loads(r.text)['candidates'][0]['content']['parts'][0]

        return txt
