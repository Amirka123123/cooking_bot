import sqlite3

from telebot import TeleBot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

from constants import get_kitchen_query_japan
from utils import buttons_for_keyboard_japanese_kitchen, ingredients_for_foods, check_name_food

TOKEN = "6290184537:AAHsxexwzfKz95Y_vSd51KHGIuwE9zlRVoU"

bot = TeleBot(TOKEN, parse_mode="MARKDOWN")


def main_menu(): #первоначальная клавиатура
    search_button = KeyboardButton("Search🔎")
    kitchen_button = KeyboardButton("Foreign kitchens🍜")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(search_button)
    keyboard.add(kitchen_button)

    return keyboard


def kitchen_menu_keyboard(): # keyboards with several kitchen meals
    japan_kitchen = KeyboardButton("Japanese Food🍱")
    european_kitchen = KeyboardButton("European Food🍟")
    korean_kitchen = KeyboardButton("Korean Food🍘")
    italian_kitchen = KeyboardButton("Italian Food🧀")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(japan_kitchen)
    keyboard.add(european_kitchen)
    keyboard.add(korean_kitchen)
    keyboard.add(italian_kitchen)

    return keyboard


def keyboard_with_japan_food():
    data = buttons_for_keyboard_japanese_kitchen()
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for datum in data:
        print(datum)
        button1 = KeyboardButton(datum[1])
        keyboard.add(button1)

    return keyboard


def get_kitchen_product() -> list:
    kitchens = []

    try:
        conn = sqlite3.connect("kitchendatabasebot.db`")
        cursor = conn.cursor()
        sql = get_kitchen_query_japan()
        cursor.execute(sql)

        for Japanese_food in cursor.fetchall():
            kitchens.append(Japanese_food[0])

    except Exception as e:
        print(e)

    return kitchens


@bot.message_handler(func=lambda message: message.text == "Japanese Food🍱")
def japan_food(message):
    reply = "Choose your food:"
    bot.reply_to(message, reply, reply_markup=keyboard_with_japan_food())


@bot.message_handler(func=lambda message: message.text in check_name_food())
def ingredients_for_sushi(message):
    ingr, descr = ingredients_for_foods(message.text)
    description = f"""*Description:* {descr}\n \n*Ingredients:* {ingr}"""
    photo = open('photos/download.jpeg', 'rb')
    print(photo)
    bot.send_photo(message.chat.id, photo, caption=description, parse_mode='MARKDOWN')


@bot.message_handler(func=lambda message: message.text == "/start")
def welcome(message):
    reply = "Hi there! This bot will help you to find the ingredients for foreign meals!"
    bot.reply_to(message, reply, reply_markup=main_menu())


@bot.message_handler(func=lambda message: message.text == "Foreign kitchens🍜")
def send_message_after_main_menu(message):
    reply = "Let's choose something!✨"
    bot.reply_to(message, reply, reply_markup=kitchen_menu_keyboard())


bot.infinity_polling()
