import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos').json()
print(response[7])

superheroes = requests.get('https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json').json()
print(superheroes)
