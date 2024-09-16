import json as js

from urllib.request import urlopen

url = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
dados = js.loads(url)[0]

print('Título:', dados['title'])
print('URL:', dados['url'])
print('Duração:', dados['duration'])
print('Nº de visualizações:', dados['stats_number_of_plays'])