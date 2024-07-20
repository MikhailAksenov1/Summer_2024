import telebot
import random
import bs4
import urllib3

TOKEN = '*************************************'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_hello(message):
    bot.reply_to(message, "Привет, если ты хочешь получить задачу, то нажми /task:)")


@bot.message_handler(commands=['task'])
def send_task(message):
    link_to_send = random.choice(links_to_excersises)
    bot.reply_to(message, f'Окей, решайте вот эту задачу — {link_to_send}')


site = urllib3.request('GET', "https://pythonist.ru/category/tasks/coding-tasks/")
site = site.data.decode('utf-8')

soup = bs4.BeautifulSoup(site, features="html.parser")

raw_excersises = soup.find('div', {"class": 'content-area'})  # забираем интересующий нас кусок кода
excersises = raw_excersises.find_all('div', {"class": 'list-article-content'})

links_to_excersises = []
for i in range(len(excersises)):
    links_to_excersises.append(excersises[i].find('h2', {"class": 'entry-title'}).find('a').get('href'))

while True:  # Для постоянной работы
    bot.polling()
