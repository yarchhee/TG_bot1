# Сделать 3 запроса по 3м адресам и получить странички
# сохранить их в словарик где ключами являются названия страниц

import requests
s = requests.get("https://kompege.ru/variant?kim=25154796")
a = requests.get("https://dnevnik.edumil.ru/component/dnevnik/?controller=dnevnik&task=dnevnik")
b = requests.get("https://kompege.ru/task")
print(b.text)
dict = {}
dict['dnevnik'] = a.text
dict['tasks'] = b.text
dict['varik'] = s.text


