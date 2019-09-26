import requests

#Возвращает список предстоящих проходов МКС для определенного местоположения ﻿
parameters = {"lat": 54.43, "lon": 20.30,"n":5}
r1 = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(r1.content)
print(r1.text)
print(r1.url)


#возвращает текущее количество людей в космосе
r2=requests.get('http://api.open-notify.org/astros.json')
print(r2.content)
print(r2.text)
print(r2.url)

