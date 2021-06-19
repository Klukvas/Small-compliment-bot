from typing import KeysView
from warnings import resetwarnings
import requests
import json
from bs4 import BeautifulSoup
from random import randint
from re import search
import threading
import telebot
bot = telebot.TeleBot('1828049312:AAE5IaifKUPu53fSQmQwa2ti3KltWA3V95c')

def free_generator():
    response = json.loads( requests.get("http://free-generator.ru/generator.php?action=compliment&pol=1&type=2").text )
    message = response['compliment']["compliment"]
    return message

def kompli_me_get_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,  "lxml")
    max_page = soup.find_all('a', class_='page-numbers')
    if len(max_page) > 1:
        max_page = max_page[1].get("href").split('/')[-1]
    else:
        max_page = None
    return max_page

def kompli_me_devushka() -> list:
    url = 'http://kompli.me/devushka'
    max_page = kompli_me_get_page(url)
    if max_page is not None:
        ch_pg = randint(1, int(max_page))
        if ch_pg != 1:
            url = url + f'/page/{ch_pg}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,  "lxml")
    all_komp = soup.find_all('span', itemprop = 'headline')
    all_komp = [item.text for item in all_komp]
    digi = search(r'\d', url)
    if digi == None:
        all_komp = all_komp[1:]
    return all_komp

def komplimenty_proze() -> list:
    url = 'http://kompli.me/komplimenty-v-proze'
    max_page = kompli_me_get_page(url)
    if max_page is not None:
        ch_pg = randint(1, int(max_page))
        if ch_pg != 1:
            url = url + f'/page/{ch_pg}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,  "lxml")
    all_komp = soup.find_all('span', itemprop = 'headline')
    all_komp = [item.text for item in all_komp]
    digi = search(r'\d', url)
    if digi == None:
        all_komp = all_komp[1:]
    return all_komp

def komplimenty_devochke() -> list:
    url = 'http://kompli.me/komplimenty-devochke'
    max_page = kompli_me_get_page(url)
    if max_page is not None:
        ch_pg = randint(1, int(max_page))
        if ch_pg != 1:
            url = url + f'/page/{ch_pg}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,  "lxml")
    all_komp = soup.find_all('span', itemprop = 'headline')
    all_komp = [item.text for item in all_komp]
    digi = search(r'\d', url)
    if digi == None:
        all_komp = all_komp[1:]
    return all_komp

def komplimenty_devushke() -> list:
    url = 'http://kompli.me/komplimenty-devushke'
    max_page = kompli_me_get_page(url)
    if max_page is not None:
        ch_pg = randint(1, int(max_page))
        if ch_pg != 1:
            url = url + f'/page/{ch_pg}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,  "lxml")
    all_komp = soup.find_all('span', itemprop = 'headline')
    all_komp = [item.text for item in all_komp]
    digi = search(r'\d', url)
    if digi == None:
        all_komp = all_komp[1:]
    return all_komp

def komplimenty_zhenshhine() -> list:
    url = 'http://kompli.me/komplimenty-zhenshhine'
    max_page = kompli_me_get_page(url)
    if max_page is not None:
        ch_pg = randint(1, int(max_page))
        if ch_pg != 1:
            url = url + f'/page/{ch_pg}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,  "lxml")
    all_komp = soup.find_all('span', itemprop = 'headline')
    all_komp = [item.text for item in all_komp]
    digi = search(r'\d', url)
    if digi == None:
        all_komp = all_komp[1:]
    return all_komp

def komplimenty_lyubimoj() -> list:
    url = 'http://kompli.me/komplimenty-lyubimoj'
    max_page = kompli_me_get_page(url)
    if max_page is not None:
        ch_pg = randint(1, int(max_page))
        if ch_pg != 1:
            url = url + f'/page/{ch_pg}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,  "lxml")
    all_komp = soup.find_all('span', itemprop = 'headline')
    all_komp = [item.text for item in all_komp]
    digi = search(r'\d', url)
    if digi == None:
        all_komp = all_komp[1:]
    return all_komp

def komplimenty_podruge() -> list:
    url = 'http://kompli.me/komplimenty-podruge'
    max_page = kompli_me_get_page(url)
    if max_page is not None:
        ch_pg = randint(1, int(max_page))
        if ch_pg != 1:
            url = url + f'/page/{ch_pg}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,  "lxml")
    all_komp = soup.find_all('span', itemprop = 'headline')
    all_komp = [item.text for item in all_komp]
    digi = search(r'\d', url)
    if digi == None:
        all_komp = all_komp[1:]
    return all_komp

def komplimenty_stixax() -> list:
    url = 'http://kompli.me/komplimenty-v-stixax'
    max_page = kompli_me_get_page(url)
    if max_page is not None:
        ch_pg = randint(1, int(max_page))
        if ch_pg != 1:
            url = url + f'/page/{ch_pg}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text,  "lxml")
    all_komp = soup.find_all('div', class_ = 'post-card__description')
    all_komp = [item.text for item in all_komp]
    digi = search(r'\d', url)
    if digi == None:
        all_komp = all_komp[1:]
    return all_komp

def from_file():
    with open('tt.txt', encoding='utf8') as f:
        lines = f.readlines()
        all_komp = [item.replace(' \n', '') for item in lines if len(item) > 3]
    return all_komp

def choise():
    weight = {
        1:from_file,
        2:komplimenty_stixax,
        3:komplimenty_podruge,
        4:komplimenty_lyubimoj,
        5:komplimenty_zhenshhine,
        6:komplimenty_devushke,
        7:komplimenty_devochke,
        8:komplimenty_proze,
        9:kompli_me_devushka,
        10:free_generator 
    }
    rnd = randint(1, 10)
    try:
        all_komp = weight[rnd]()
        if type(all_komp) == list:
            rnd_komp = randint(0, len(all_komp))
            komp = all_komp[rnd_komp].replace('\n', '')
        else:
            komp = all_komp
    except:
        try:
            all_komp = from_file()
            rnd_komp = randint(0, len(all_komp))
            komp = all_komp[rnd_komp].replace('\n', '')
        except:
            komp = 'Я немного сломался, но ты не переживай, меня скоро починят.\nХорошего тебе дня, человек!'
    finally:
        return komp


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    with open('chats_ids.txt', 'r') as f:
        all_ids = f.readline().split(',')
    print(all_ids)
    if not str(message.from_user.id) in all_ids: 
        with open('chats_ids.txt', 'a') as f:
            f.write(f'{message.from_user.id},')
    bot.send_message(message.from_user.id, f'Привет!Я небольшой бот, надеюсь смогу тебя порадовать.')
    send()
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.reply_to(message, 'Извини, но тут пишу только я)')

@bot.message_handler(content_types=['audio'])
def reply_to_audio(message):
    bot.reply_to(message, 'Ох уж єтот прекрасный голос')
def send():
    with open('chats_ids.txt') as f:
        ids = set(f.readline().split(','))
        message = choise()
        for id in ids:
            if len(id) > 4:
                bot.send_message(int(id), message)
    t = threading.Timer(1800.0, send)
    t.start()
    return
    
if __name__ == '__main__':
    t = threading.Timer(1800.0, send)
    t.start()
    bot.polling(none_stop=True, timeout=20)
    