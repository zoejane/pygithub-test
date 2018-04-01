import requests
import json
r = requests.get('https://api.github.com/repos/zoejane/pygithub-test')
if(r.ok):
    repoItem = json.loads(r.text)
    print(repoItem['name'])
    print("repository created: ")
    print(repoItem['created_at'])