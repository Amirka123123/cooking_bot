import sqlite3

from telebot import TeleBot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup

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


@bot.message_handler(func=lambda message: message.text == "/start")
def welcome(message):
    reply = "Hi there! This bot will help you to find the ingredients for foreign meals!"
    bot.reply_to(message, reply, reply_markup=main_menu())


@bot.message_handler(func=lambda message: message.text == "Foreign kitchens🍜")
def send_message_after_main_menu(message):
    reply = "Let's choose something!✨"
    bot.reply_to(message, reply, reply_markup=kitchen_menu_keyboard())


bot.infinity_polling()