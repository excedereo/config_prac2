import json

print("MATPLOTLIB")
import urllib.request
url = "https://pypi.org/pypi/matplotlib/json"
data = json.loads(urllib.request.urlopen(url).read())
info = data['info']
print("Версия:", info['version'])
print("Автор:", info['author'])
print("Основные элементы info:")
for key in ['version', 'author', 'requires_python', 'license', 'home_page']:
    if key in info: print(f"  {key}: {info[key]}")
print("----------------------------")
print("EXPRESS")
import urllib.request
url = "https://registry.npmjs.org/express"
data = json.loads(urllib.request.urlopen(url).read())
latest = data['versions'][data['dist-tags']['latest']]
print("Версия:", latest['version'])
print("Автор:", latest['author'])
print("Основные элементы package.json:")
for key in ['name', 'version', 'main', 'description', 'license']:
    if key in latest: print(f"  {key}: {latest[key]}")