
import requests

from bs4 import BeautifulSoup



url = 'https://store.steampowered.com/app/271590/Grand_Theft_Auto_V/' #Ссылка на игру


r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser') #Берет из html страницы

price = soup.find('div', class_='discount_final_price').text #Получает цену




TOKEN_INFO = 'token'
id_chat = 'id_chat'
message_is = 'Игра с ценой - ' +  str( price) +'\n'+ url
requests.get('https://api.telegram.org/bot{}/sendMessage'.format(TOKEN_INFO), #Отправляет сообщение
             params=dict(chat_id=id_chat, text=message_is))

