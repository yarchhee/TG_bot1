import requests
from config import Config, load_config

config: Config = load_config()
bot_token = config.bot.token
# GET - на получение данных с серверов
# POST - отправляем данные на севрер или сохраняем
# 200 - ура 201
# 404 500 412
# response = requests.get("https://google.com")
# print(response.text)

s = requests.get(f"https://api.telegram.org/bot{bot_token}/getMe")
print(s.text)
# JSON