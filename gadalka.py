
import sqlite3

import requests

import json

import markups

import sqlite3

import random

import telebot

from telebot import types

magsfer1 = ["Ёще как!","Ответ очевиден-да!","Есть шанс","Возможно","Неуверен","Рак на горе еще не свистел!","Конечто нет!","Даже ёжу понятно что нет!"]
kto1 = ["Олег","Григорий","Екатерина","Ты","Константин","я","Кирил","кот","собака","Варвара","Алиса","Георгий","Никита","Дмитрий","Ярослав","Станислав","Мирослав","Александр","Маша","Алексей","Светлана","Дарья","Анастасия","София","Килограм Кириешек","Мама","Отец","ИИ","Антон","Арсений","Анатолий","Андрей","Аркадий"]
chto_delat1 = ["Загугли","стыбзить батину машину и уехать жить в ЛОНДОН" ,"изменить состав материи ","купить слабительного и подмешать врагу ","изобрести машину времени","дать люлей детям с колонкой","Снимать штаны и бегать"]
kogda1 = ["вчера" ,"позавчера","2 года назад","Олег","Завтра","После-завтра","На этой неделе","На следующей неделе","В этом месяце","В этом году"]
chto1 = ["через плечё","предлагаю 1 вариант","предлагаю 2 вариант","точно 3","неуверен но думаю 4","думаю 5","выбирай 6"]
kakoy1 = ["цветной","первый","последний","черно-белый","мощный","слабый","болеющий","здоровый как медведь","типичный Олег"]
gde1 = ["в канаве","в ресторане!","дома","на работе","в школе","на улице","на тумбочке","в вк"]
a1488 = ["1488"]
bot = telebot.TeleBot('6922176515:AAHr8GDq5sUmnr0nt3_G_g2BOv9Ud4_acLE')
@bot.message_handler(commands=['start'])
def main(message):
  markup = types.ReplyKeyboardMarkup()
  btn1 = types.KeyboardButton('Наш сайт "Гадалка" : http://127.0.0.1:8000/')
  markup.row(btn1)
  bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name}, меня зовут gadalka, я чат бот. Для дальнейшего использования напишите /help', reply_markup = markup)
  bot.register_next_step_handler(message)
@bot.message_handler(commands=['help'])
def main(message):
  markup = types.ReplyKeyboardMarkup()
  btn1 = types.KeyboardButton('/start')
  btn2 = types.KeyboardButton('/gadanie')
  btn3 = types.KeyboardButton('/instrukciya')
  btn4 = types.KeyboardButton('/primer')
  markup.row(btn1, btn2)
  markup.row(btn3, btn4)
  bot.send_message(message.chat.id, "Привет я помогу тебе если тебе надо. Вот список доступных команд: /start начать использовать бота, /gadanie ты должен будешь выбрать один из вариантов и я погадаю тебе,/instrukciya показывает инструкцию, /primer показывает моих братьев", reply_markup = markup )

@bot.message_handler(commands=['primer'])
def primer(message):
  markup = types.ReplyKeyboardMarkup()
  btn1=types.KeyboardButton('пример', url = 't.me/OgurrecBot')
  markup.row(btn1)
  bot.reply_to(message, 'это мои братья', reply_markup=markup)

@bot.message_handler(commands=['instrukciya'])
def main(message):
  bot.send_message(message.chat.id, "Это инструкция по использованию бота. Так что читайте внимательно чтобы понять как работает бот бот:@Rokan358358. Бот начинает свою работу и после этого он приветствует тебя, потом вы должны прописать команду /help чтобы понять что он может делать и только после это надо выбрать одну из команд там есть только 3 команды а именно /primer - показывает наши прошлые проекты, /gadanie – эта команда главная в этом боте, про неё поговорим позже и третья команда это /start — начинает работу бота. Теперь поговорим подробнее о команде /gadanie в этой команде бот отправляет несколько вопросов вы должны выбрать один из них каждый вопрос имеет несколько ответов надо написать одно из этих вопросов: Вопрос да/нет — на этот вопрос он будет отвечать да или нет. Вопрос кто? - ответит на этот вопрос кто сделал, кто сделали. Вопрос что делать? - даст вам ответ что вам сделать или делать или нет. Вопрос когда? - он ответит когда случилось,случится,случается в то или оное время. Вопрос что? - он ответит на один из ваших вариантов. Вопрос какой? - он ответит какой/какая он/она/оно. Вопрос где? - он ответит тебе где он/она/оно. Как итог этот бот имеет 4 команды и на команду /gadanie у бота есть 7 вопросов и на каждый вопрос есть много ответов. Огромное спасибо моей команде: Дмитрий Александров- главный кодер, Степан Сукманов- художник, Савелий Хромов- помощник кодера. И спасибо нашему преподавателю: Никита Долголенко.(Бот был создан на python)")
  bot.register_next_step_handler(message)

@bot.message_handler(commands=['gadanie'])
def main(message):
  markup = types.ReplyKeyboardMarkup()
  btn1 = types.KeyboardButton('Вопрос да/нет')
  btn2 = types.KeyboardButton('Вопрос кто?')
  btn3 = types.KeyboardButton('Вопрос что делать?')
  btn4 = types.KeyboardButton('Вопрос когда?')
  btn5 = types.KeyboardButton('Вопрос что?')
  btn6 = types.KeyboardButton('Вопрос какой?')
  btn7 = types.KeyboardButton('Вопрос где?')
  btn8 = types.KeyboardButton('/primer')
  markup.row(btn1, btn2)
  markup.row(btn3, btn4)
  bot.send_message(message.chat.id, 'Выбери вопрос всей твоей жизни! Чтобы написать вопросы нужно сначала выбрать ВИД вопроса. И только потом нужно задавать свой вопрос. Можно выбрать вопросы: (Вопрос кто?): (Вопрос что делать?): (Вопрос когда?): (Вопрос что?): (Вопрос какой?): (Вопрос где?): (Вопрос да/нет): писать без скобок.')
  bot.register_next_step_handler(message, on_click)

def on_click(message):
  if message.text=='Вопрос да/нет':
    magsfer2 = message.text.strip().lower()
    bot.send_message(message.chat.id, 'Ты выбрал вопрос да/нет, задавай вопрос на который я тебе отвечу тебе да или нет.')

    @bot.message_handler(content_types=['text'])
    def main(message):
      magsfer3 = random.choice(magsfer1)
      bot.send_message(message.chat.id, magsfer3)


  elif message.text=='Вопрос кто?':
    gadanie2 = message.text.strip().lower()
    bot.send_message(message.chat.id, 'Ты выбрал вопрос кто, задавай вопрос, я отвечу тебе кто сделал то что ты спросил.')

    @bot.message_handler(content_types=['text'])
    def main(message):
      gadanie3 = random.choice(kto1)
      bot.send_message(message.chat.id, gadanie3)


  elif message.text=='Вопрос что делать?':
    gadanie_2 = message.text.strip().lower()
    bot.send_message(message.chat.id, 'Ты выбрал вопрос что сделать, задавай вопрос и я отвечу что тебе сделать.')

    @bot.message_handler(content_types=['text'])
    def main(message):
      gadanie_3 = random.choice(chto_delat1)
      bot.send_message(message.chat.id, gadanie_3)

  elif message.text=='Вопрос когда?':
    gadanie4 = message.text.strip().lower()
    bot.send_message(message.chat.id, 'Ты выбрал вопрос когда, задавай вопрос и я отвечу тебе когда случилось(случиться/случается) в то или оное время.')

    @bot.message_handler(content_types=['text'])
    def main(message):
      gadanie5 = random.choice(kogda1)
      bot.send_message(message.chat.id, gadanie5)

  elif message.text=='Вопрос что?':
    gadanie_4 = message.text.strip().lower()
    bot.send_message(message.chat.id, 'Ты выбрал вопрос что, задай мне несколько ответов и я выберу один из них.')

    @bot.message_handler(content_types=['text'])
    def main(message):
      gadanie_5 = random.choice(chto1)
      bot.send_message(message.chat.id, gadanie_5)

  elif message.text=='Вопрос какой?':
    gadanie6 = message.text.strip().lower()
    bot.send_message(message.chat.id, 'Ты выбрал вопрос какой, задавай вопрос и я отвечу какой он/она/оно.')

    @bot.message_handler(content_types=['text'])
    def main(message):
      gadanie7 = random.choice(kakoy1)
      bot.send_message(message.chat.id, gadanie7)

  elif message.text=='Вопрос где?':
    gadanie_6 = message.text.strip().lower()
    bot.send_message(message.chat.id, 'Ты выбрал вопрос где, задавай вопрос и я отвечу где он/она/оно.')

    @bot.message_handler(content_types=['text'])
    def main(message):
      gadanie_7 = random.choice(gde1)
      bot.send_message(message.chat.id, gadanie_7)

bot.infinity_polling()